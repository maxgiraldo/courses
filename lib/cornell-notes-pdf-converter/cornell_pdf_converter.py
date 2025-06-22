#!/usr/bin/env python3
"""
Cornell Notes PDF Converter

Converts Cornell-style notes written in markdown format to professionally 
formatted PDF documents with LaTeX mathematical equation support.
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Any

import markdown
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, 
    PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY


class CornellNotesPDFConverter:
    """Main converter class for Cornell Notes to PDF conversion."""
    
    def __init__(self, output_filename: str, page_size: str = "letter"):
        """
        Initialize the converter.
        
        Args:
            output_filename: Name of the output PDF file
            page_size: Page size ('letter' or 'a4')
        """
        self.output_filename = output_filename
        self.page_size = A4 if page_size.lower() == 'a4' else letter
        self.doc = SimpleDocTemplate(
            output_filename,
            pagesize=self.page_size,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=1*inch,
            bottomMargin=1*inch
        )
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()
        self.story = []
        
    def setup_custom_styles(self):
        """Define custom paragraph styles for different content types."""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=18,
            spaceAfter=12,
            textColor=colors.darkblue,
            alignment=TA_CENTER
        ))
        
        # Section header style
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=14,
            spaceAfter=6,
            spaceBefore=12,
            textColor=colors.red,
            leftIndent=0
        ))
        
        # Cue column style (bold, smaller)
        self.styles.add(ParagraphStyle(
            name='CueColumn',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.black,
            alignment=TA_LEFT,
            fontName='Helvetica-Bold'
        ))
        
        # Notes column style
        self.styles.add(ParagraphStyle(
            name='NotesColumn',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.black,
            alignment=TA_LEFT,
            leftIndent=0
        ))
        
        # Summary style
        self.styles.add(ParagraphStyle(
            name='Summary',
            parent=self.styles['Normal'],
            fontSize=10,
            alignment=TA_JUSTIFY,
            spaceBefore=6,
            spaceAfter=6,
            leftIndent=0.25*inch,
            rightIndent=0.25*inch
        ))
        
    def clean_latex_for_pdf(self, text: str) -> str:
        """
        Convert LaTeX mathematical expressions to Unicode characters for PDF.
        
        Args:
            text: Input text with LaTeX expressions
            
        Returns:
            Text with LaTeX converted to Unicode
        """
        # Greek letters mapping
        greek_letters = {
            r'\\alpha': 'α', r'\\beta': 'β', r'\\gamma': 'γ', r'\\delta': 'δ',
            r'\\epsilon': 'ε', r'\\varepsilon': 'ε', r'\\zeta': 'ζ', r'\\eta': 'η',
            r'\\theta': 'θ', r'\\iota': 'ι', r'\\kappa': 'κ', r'\\lambda': 'λ',
            r'\\mu': 'μ', r'\\nu': 'ν', r'\\xi': 'ξ', r'\\pi': 'π',
            r'\\rho': 'ρ', r'\\sigma': 'σ', r'\\tau': 'τ', r'\\upsilon': 'υ',
            r'\\phi': 'φ', r'\\chi': 'χ', r'\\psi': 'ψ', r'\\omega': 'ω',
            r'\\Gamma': 'Γ', r'\\Delta': 'Δ', r'\\Theta': 'Θ', r'\\Lambda': 'Λ',
            r'\\Xi': 'Ξ', r'\\Pi': 'Π', r'\\Sigma': 'Σ', r'\\Phi': 'Φ',
            r'\\Psi': 'Ψ', r'\\Omega': 'Ω'
        }
        
        # Mathematical symbols
        math_symbols = {
            r'\\pm': '±', r'\\mp': '∓', r'\\times': '×', r'\\div': '÷',
            r'\\leq': '≤', r'\\geq': '≥', r'\\neq': '≠', r'\\approx': '≈',
            r'\\equiv': '≡', r'\\sim': '∼', r'\\propto': '∝',
            r'\\rightarrow': '→', r'\\leftarrow': '←', r'\\Rightarrow': '⇒',
            r'\\Leftarrow': '⇐', r'\\leftrightarrow': '↔',
            r'\\infty': '∞', r'\\partial': '∂', r'\\nabla': '∇',
            r'\\sum': '∑', r'\\prod': '∏', r'\\int': '∫'
        }
        
        # Process inline math $...$
        def process_inline_math(match):
            math_content = match.group(1)
            
            # Apply Greek letters
            for latex, unicode_char in greek_letters.items():
                math_content = re.sub(latex, unicode_char, math_content)
            
            # Apply math symbols
            for latex, unicode_char in math_symbols.items():
                math_content = re.sub(latex, unicode_char, math_content)
            
            # Handle subscripts r_{i,t} -> r[i,t]
            math_content = re.sub(r'([a-zA-Z])_\{([^}]+)\}', r'\1[\2]', math_content)
            math_content = re.sub(r'([a-zA-Z])_([a-zA-Z0-9])', r'\1[\2]', math_content)
            
            # Handle superscripts x^2 -> x²
            superscript_map = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', 
                             '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}
            for digit, sup in superscript_map.items():
                math_content = re.sub(rf'\^{digit}', sup, math_content)
            
            # Handle fractions \frac{a}{b} -> (a)/(b)
            math_content = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1)/(\2)', math_content)
            
            # Handle square roots \sqrt{x} -> √x
            math_content = re.sub(r'\\sqrt\{([^}]+)\}', r'√\1', math_content)
            
            return math_content
        
        # Process block math $$...$$
        def process_block_math(match):
            math_content = process_inline_math(match)
            return f"\n{math_content}\n"
        
        # Apply transformations
        text = re.sub(r'\$\$([^$]+)\$\$', process_block_math, text)
        text = re.sub(r'\$([^$]+)\$', process_inline_math, text)
        
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
                            clean_cue = self.clean_latex_for_pdf(clean_cue)
                            clean_notes = self.clean_latex_for_pdf(' '.join(current_notes))
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
            clean_cue = self.clean_latex_for_pdf(clean_cue)
            clean_notes = self.clean_latex_for_pdf(' '.join(current_notes))
            pairs.append((clean_cue, clean_notes))
        
        return pairs
    
    def process_markdown_content(self, content: str):
        """
        Process markdown content and convert to PDF elements.
        
        Args:
            content: Markdown content string
        """
        sections = content.split('---')
        
        for section in sections:
            section = section.strip()
            if not section:
                continue
                
            lines = section.split('\n')
            i = 0
            
            while i < len(lines):
                line = lines[i].strip()
                
                # Main title (# Title)
                if line.startswith('# '):
                    title = line[2:].strip()
                    title = self.clean_latex_for_pdf(title)
                    self.story.append(Paragraph(title, self.styles['CustomTitle']))
                    self.story.append(Spacer(1, 12))
                
                # Section header (## Section)
                elif line.startswith('## '):
                    header = line[3:].strip()
                    header = self.clean_latex_for_pdf(header)
                    self.story.append(Paragraph(header, self.styles['SectionHeader']))
                    self.story.append(Spacer(1, 6))
                
                # Cornell table header (### Cue Column | Notes Section)
                elif line.startswith('### ') and '|' in line:
                    # Skip the header line and separator
                    i += 1
                    if i < len(lines) and '---' in lines[i]:
                        i += 1
                    
                    # Collect table content
                    table_content = []
                    while i < len(lines) and lines[i].strip():
                        table_content.append(lines[i])
                        i += 1
                    
                    # Parse and create table
                    if table_content:
                        pairs = self.parse_cornell_table('\n'.join(table_content))
                        if pairs:
                            self.create_cornell_table(pairs)
                    continue
                
                # Summary section (starts with ## Summary)
                elif line.startswith('## Summary'):
                    i += 1
                    summary_content = []
                    while i < len(lines) and lines[i].strip():
                        summary_content.append(lines[i].strip())
                        i += 1
                    
                    if summary_content:
                        summary_text = ' '.join(summary_content)
                        summary_text = self.clean_latex_for_pdf(summary_text)
                        self.story.append(Paragraph(f"<b>Summary:</b> {summary_text}", 
                                                  self.styles['Summary']))
                        self.story.append(Spacer(1, 12))
                    continue
                
                # Regular paragraph
                elif line and not line.startswith('#'):
                    line = self.clean_latex_for_pdf(line)
                    self.story.append(Paragraph(line, self.styles['Normal']))
                    self.story.append(Spacer(1, 6))
                
                i += 1
            
            # Add page break between major sections
            if section != sections[-1]:
                self.story.append(PageBreak())
    
    def create_cornell_table(self, pairs: List[Tuple[str, str]]):
        """
        Create a Cornell-style table from cue/notes pairs.
        
        Args:
            pairs: List of (cue, notes) tuples
        """
        if not pairs:
            return
            
        # Prepare table data
        table_data = []
        
        for cue, notes in pairs:
            # Format notes with bullet points on separate lines
            formatted_notes = notes.replace(' • ', '<br/>• ')
            
            cue_para = Paragraph(cue, self.styles['CueColumn'])
            notes_para = Paragraph(formatted_notes, self.styles['NotesColumn'])
            table_data.append([cue_para, notes_para])
        
        # Create table with proper column widths for letter size
        available_width = self.page_size[0] - 1.5*inch  # Account for margins
        cue_width = available_width * 0.3  # 30% for cue column
        notes_width = available_width * 0.7  # 70% for notes column
        
        table = Table(table_data, colWidths=[cue_width, notes_width])
        
        # Apply table styling
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (0, -1), 'LEFT'),      # Cue column left align
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),      # Notes column left align
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),  # Cue column bold
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),       # Notes column normal
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            # Different background colors for distinction
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),  # Cue column light grey
            ('BACKGROUND', (1, 0), (1, -1), colors.white),      # Notes column white
        ]))
        
        self.story.append(KeepTogether(table))
        self.story.append(Spacer(1, 12))
    
    def convert_file(self, input_file: str):
        """
        Convert a markdown file to PDF.
        
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
        Convert markdown text to PDF.
        
        Args:
            markdown_text: Markdown content as string
        """
        try:
            self.process_markdown_content(markdown_text)
            self.doc.build(self.story)
            print(f"PDF generated successfully: {self.output_filename}")
        except Exception as e:
            raise Exception(f"Error generating PDF: {str(e)}")


def main():
    """Command line interface for the converter."""
    parser = argparse.ArgumentParser(
        description="Convert Cornell-style notes from Markdown to PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cornell_pdf_converter.py notes.md
  python cornell_pdf_converter.py notes.md -o finance_notes.pdf
  python cornell_pdf_converter.py notes.md --page-size a4
        """
    )
    
    parser.add_argument('input_file', 
                       help='Input markdown file with Cornell notes')
    parser.add_argument('-o', '--output', 
                       help='Output PDF filename (default: input_file.pdf)')
    parser.add_argument('--page-size', 
                       choices=['letter', 'a4'], 
                       default='letter',
                       help='Page size for PDF (default: letter)')
    
    args = parser.parse_args()
    
    # Determine output filename
    if args.output:
        output_file = args.output
    else:
        input_path = Path(args.input_file)
        output_file = input_path.with_suffix('.pdf').name
    
    try:
        # Create converter and process file
        converter = CornellNotesPDFConverter(output_file, args.page_size)
        converter.convert_file(args.input_file)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()