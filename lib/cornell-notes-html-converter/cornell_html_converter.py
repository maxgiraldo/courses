#!/usr/bin/env python3
"""
Cornell Notes HTML Converter

Converts Cornell-style notes written in markdown format to professionally 
formatted HTML documents with LaTeX mathematical equation support using Tailwind CSS.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Any

import markdown


class CornellNotesHTMLConverter:
    """Main converter class for Cornell Notes to HTML conversion."""
    
    def __init__(self, output_filename: str):
        """
        Initialize the converter.
        
        Args:
            output_filename: Name of the output HTML file
        """
        self.output_filename = output_filename
        self.html_content = []
        
    def get_html_template(self) -> str:
        """Return the HTML template with Tailwind CSS."""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cornell Notes</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\(', '\\)']],
                displayMath: [['$$', '$$'], ['\\[', '\\]']]
            }
        };
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        'serif': ['Georgia', 'Times New Roman', 'serif'],
                        'sans': ['Inter', 'system-ui', '-apple-system', 'sans-serif']
                    }
                }
            }
        }
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .cornell-cue {
            background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            border-right: 3px solid #3b82f6;
        }
        .cornell-notes {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        }
        .cornell-table {
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
    </style>
</head>
<body class="bg-gradient-to-br from-slate-50 to-blue-50 min-h-screen font-sans">
    <div class="max-w-6xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div class="bg-white rounded-2xl shadow-xl border border-slate-200 overflow-hidden">
            <div class="px-8 py-10 sm:px-12 sm:py-12">
                {content}
            </div>
        </div>
    </div>
</body>
</html>'''
        
    def preserve_latex_for_html(self, text: str) -> str:
        """
        Preserve LaTeX mathematical expressions and process markdown formatting for HTML.
        
        Args:
            text: Input text with LaTeX expressions and markdown
            
        Returns:
            Text with LaTeX preserved and markdown converted to HTML
        """
        # Temporarily replace math expressions with placeholders
        math_expressions = []
        
        # Find and store block math $$...$$
        def store_block_math(match):
            math_expressions.append(match.group(0))
            return f"__BLOCK_MATH_{len(math_expressions) - 1}__"
        
        # Find and store inline math $...$
        def store_inline_math(match):
            math_expressions.append(match.group(0))
            return f"__INLINE_MATH_{len(math_expressions) - 1}__"
        
        # Store math expressions
        text = re.sub(r'\$\$([^$]+)\$\$', store_block_math, text)
        text = re.sub(r'\$([^$]+)\$', store_inline_math, text)
        
        # Process markdown formatting (before HTML escaping)
        # Bold text: **text** -> <strong>text</strong>
        text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
        
        # Italic text: *text* -> <em>text</em> (only single asterisks)
        # Skip this for now to avoid regex complexity - focus on bold formatting first
        # text = re.sub(r'\*([^*\$]+)\*', r'<em>\1</em>', text)
        
        # Code text: `text` -> <code>text</code>
        text = re.sub(r'`([^`]+)`', r'<code class="bg-gray-100 px-1 py-0.5 rounded text-sm font-mono">\1</code>', text)
        
        # Escape HTML characters but preserve our markdown HTML tags
        # First store our HTML tags
        html_tags = []
        def store_html_tag(match):
            html_tags.append(match.group(0))
            return f"__HTML_TAG_{len(html_tags) - 1}__"
        
        # Store HTML tags we created
        text = re.sub(r'</?(?:strong|em|code|br|span)[^>]*>', store_html_tag, text)
        
        # Now escape remaining < and > 
        text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        
        # Restore our HTML tags
        for i, html_tag in enumerate(html_tags):
            text = text.replace(f"__HTML_TAG_{i}__", html_tag)
        
        # Restore math expressions
        for i, math_expr in enumerate(math_expressions):
            if f"__BLOCK_MATH_{i}__" in text:
                text = text.replace(f"__BLOCK_MATH_{i}__", math_expr)
            elif f"__INLINE_MATH_{i}__" in text:
                text = text.replace(f"__INLINE_MATH_{i}__", math_expr)
        
        return text
    
    def parse_cornell_table(self, content: str) -> List[Tuple[str, str]]:
        """
        Parse Cornell-style table content into cue/notes pairs.
        
        Args:
            content: Table content in markdown format
            
        Returns:
            List of (cue, notes) tuples
        """
        lines = content.strip().split('\n')
        pairs = []
        current_cue = ""
        current_notes = []
        
        for line in lines:
            if '|' in line and not line.strip().startswith('---'):
                parts = line.split('|', 1)
                if len(parts) == 2:
                    cue_part = parts[0].strip()
                    notes_part = parts[1].strip()
                    
                    # If we have a new cue (not empty), save previous pair and start new one
                    if cue_part:
                        # Save previous pair if exists
                        if current_cue and current_notes:
                            clean_cue = re.sub(r'\*\*(.*?)\*\*', r'\1', current_cue)
                            clean_cue = self.preserve_latex_for_html(clean_cue)
                            clean_notes = self.preserve_latex_for_html(' '.join(current_notes))
                            pairs.append((clean_cue, clean_notes))
                        
                        # Start new pair
                        current_cue = cue_part
                        current_notes = [notes_part] if notes_part else []
                    else:
                        # Continuation of previous notes (empty cue column)
                        if notes_part:
                            current_notes.append(notes_part)
        
        # Don't forget the last pair
        if current_cue and current_notes:
            clean_cue = re.sub(r'\*\*(.*?)\*\*', r'\1', current_cue)
            clean_cue = self.preserve_latex_for_html(clean_cue)
            clean_notes = self.preserve_latex_for_html(' '.join(current_notes))
            pairs.append((clean_cue, clean_notes))
        
        return pairs
    
    def process_markdown_content(self, content: str):
        """
        Process markdown content and convert to HTML elements.
        
        Args:
            content: Markdown content string
        """
        lines = content.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and horizontal rules
            if not line or line == '---':
                i += 1
                continue
            
            # Main title (# Title)
            if line.startswith('# '):
                title = line[2:].strip()
                title = self.preserve_latex_for_html(title)
                self.html_content.append(f'<div class="text-center mb-12"><h1 class="text-4xl font-bold text-slate-800 mb-2">{title}</h1><div class="w-24 h-1 bg-gradient-to-r from-blue-500 to-blue-600 mx-auto rounded-full"></div></div>')
            
            # Section header (## Section)
            elif line.startswith('## '):
                header = line[3:].strip()
                header = self.preserve_latex_for_html(header)
                if header.lower() == 'summary':
                    self.html_content.append(f'<h2 class="text-2xl font-bold text-slate-700 mt-12 mb-6 pb-2 border-b-2 border-red-200">{header}</h2>')
                    i += 1
                    # Skip any empty lines after the summary header
                    while i < len(lines) and not lines[i].strip():
                        i += 1
                    
                    summary_content = []
                    while i < len(lines) and lines[i].strip():
                        summary_content.append(lines[i].strip())
                        i += 1
                    
                    if summary_content:
                        summary_text = ' '.join(summary_content)
                        summary_text = self.preserve_latex_for_html(summary_text)
                        self.html_content.append(f'<div class="bg-gradient-to-r from-blue-50 to-indigo-50 border-l-4 border-blue-500 rounded-r-lg p-6 mb-8 shadow-sm"><p class="text-slate-700 leading-relaxed text-base">{summary_text}</p></div>')
                    continue
                else:
                    self.html_content.append(f'<h2 class="text-2xl font-bold text-slate-700 mt-12 mb-6 pb-2 border-b-2 border-red-200">{header}</h2>')
            
            # Cornell table header (### Cue Column | Notes Section)
            elif line.startswith('### ') and '|' in line:
                # Skip the header line and separator
                i += 1
                if i < len(lines) and '---' in lines[i]:
                    i += 1
                
                # Collect table content until we hit an empty line or next section
                table_content = []
                while i < len(lines):
                    current_line = lines[i].strip()
                    if not current_line or current_line == '---':
                        break
                    if current_line.startswith('#'):
                        i -= 1  # Back up so the header gets processed
                        break
                    table_content.append(lines[i])
                    i += 1
                
                # Parse and create table
                if table_content:
                    pairs = self.parse_cornell_table('\n'.join(table_content))
                    if pairs:
                        self.create_cornell_table_html(pairs)
                continue
            
            # Alternative Cornell format: lines starting with "- text |"
            elif line.startswith('- ') and '|' in line:
                # Collect all consecutive lines with this format
                cornell_pairs = []
                while i < len(lines) and lines[i].strip():
                    current_line = lines[i].strip()
                    if current_line.startswith('- ') and '|' in current_line:
                        # Parse this line as cue | notes
                        parts = current_line[2:].split('|', 1)  # Remove "- " and split
                        if len(parts) == 2:
                            cue = parts[0].strip()
                            notes = parts[1].strip()
                            cue = self.preserve_latex_for_html(cue)
                            notes = self.preserve_latex_for_html(notes)
                            cornell_pairs.append((cue, notes))
                    elif current_line.startswith('|'):
                        # Continuation line for previous notes
                        if cornell_pairs:
                            continuation = current_line[1:].strip()  # Remove "|"
                            continuation = self.preserve_latex_for_html(continuation)
                            # Append to last notes entry
                            last_cue, last_notes = cornell_pairs[-1]
                            cornell_pairs[-1] = (last_cue, last_notes + '<br/>' + continuation)
                    else:
                        break
                    i += 1
                
                # Create table from collected pairs
                if cornell_pairs:
                    self.create_cornell_table_html(cornell_pairs)
                continue
            
            # Regular paragraph
            elif line and not line.startswith('#'):
                line = self.preserve_latex_for_html(line)
                self.html_content.append(f'<p class="text-slate-700 leading-relaxed mb-4">{line}</p>')
            
            i += 1
    
    def create_cornell_table_html(self, pairs: List[Tuple[str, str]]):
        """
        Create a Cornell-style HTML table from cue/notes pairs.
        
        Args:
            pairs: List of (cue, notes) tuples
        """
        if not pairs:
            return
        
        # Start the Cornell table with enhanced styling
        html_table = ['<div class="mb-8">']
        html_table.append('<div class="cornell-table rounded-lg overflow-hidden border border-slate-300">')
        html_table.append('<table class="w-full">')
        
        for i, (cue, notes) in enumerate(pairs):
            # Format notes with proper bullet points and line breaks
            formatted_notes = notes.replace(' • ', '<br/><span class="inline-block w-4">•</span>')
            if not formatted_notes.startswith('<br/>'):
                formatted_notes = '<span class="inline-block w-4">•</span>' + formatted_notes[1:] if formatted_notes.startswith('•') else formatted_notes
            
            # Add border bottom except for last row
            border_class = 'border-b border-slate-200' if i < len(pairs) - 1 else ''
            
            html_table.append(f'<tr class="{border_class}">')
            html_table.append(f'<td class="cornell-cue w-1/3 px-6 py-4 font-semibold text-slate-700 text-sm leading-relaxed align-top">{cue}</td>')
            html_table.append(f'<td class="cornell-notes w-2/3 px-6 py-4 text-slate-800 text-sm leading-relaxed align-top">{formatted_notes}</td>')
            html_table.append('</tr>')
        
        html_table.append('</table>')
        html_table.append('</div>')
        html_table.append('</div>')
        
        self.html_content.append('\n'.join(html_table))
    
    def convert_file(self, input_file: str):
        """
        Convert a markdown file to HTML.
        
        Args:
            input_file: Path to input markdown file
        """
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            self.convert_text(content)
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file '{input_file}' not found.")
        except Exception as e:
            raise Exception(f"Error reading file '{input_file}': {str(e)}")
    
    def convert_text(self, markdown_text: str):
        """
        Convert markdown text to HTML.
        
        Args:
            markdown_text: Markdown content as string
        """
        try:
            self.process_markdown_content(markdown_text)
            
            # Generate final HTML
            content_html = '\n'.join(self.html_content)
            final_html = self.get_html_template().replace('{content}', content_html)
            
            # Write to file
            with open(self.output_filename, 'w', encoding='utf-8') as f:
                f.write(final_html)
                
            print(f"HTML generated successfully: {self.output_filename}")
        except Exception as e:
            raise Exception(f"Error generating HTML: {str(e)}")


def main():
    """Command line interface for the converter."""
    parser = argparse.ArgumentParser(
        description="Convert Cornell-style notes from Markdown to HTML",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cornell_pdf_converter.py notes.md
  python cornell_pdf_converter.py notes.md -o finance_notes.html
        """
    )
    
    parser.add_argument('input_file', 
                       help='Input markdown file with Cornell notes')
    parser.add_argument('-o', '--output', 
                       help='Output HTML filename (default: input_file.html)')
    
    args = parser.parse_args()
    
    # Determine output filename
    if args.output:
        output_file = args.output
    else:
        input_path = Path(args.input_file)
        output_file = input_path.with_suffix('.html').name
    
    try:
        # Create converter and process file
        converter = CornellNotesHTMLConverter(output_file)
        converter.convert_file(args.input_file)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()