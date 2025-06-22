# Cornell Notes HTML Converter Project

## Project Overview

This project provides a Python script that converts Cornell-style notes written in markdown format to professionally formatted HTML documents using Tailwind CSS. The converter was specifically designed to handle academic finance notes with LaTeX mathematical equations rendered via MathJax.

## Background & Use Case

The original use case involved converting Active Money Management course notes that included:
- Cornell note-taking format (cue column | notes section)
- CAPM equations and financial formulas in LaTeX
- Complex mathematical notation (Greek letters, subscripts, superscripts)
- Multiple sections with summaries

## File Structure

```
project/
├── cornell_html_converter.py   # Main conversion script
├── CONTEXT.md                  # This documentation file
├── sample_notes.md             # Example Cornell notes (finance/CAPM)
└── requirements.txt            # Python dependencies
```

## Key Features Implemented

### Cornell Note Format Support
- **Two-column layout**: Cue column (questions/keywords) | Notes column (detailed content)
- **Section headers**: Automatic formatting of `## Section Name`
- **Summary sections**: Special formatting for summary content
- **Responsive design**: Works on desktop and mobile devices

### LaTeX Math Processing
- **MathJax integration**: Full LaTeX math rendering support
- **Inline math**: `$equation$` notation
- **Block equations**: `$$equation$$` notation
- **Greek letters**: α, β, γ, ε, σ, μ, π, Δ, etc.
- **Mathematical symbols**: All LaTeX symbols supported
- **Subscripts/Superscripts**: `r_{i,t}`, `x^2` formatting
- **Fractions**: `\frac{a}{b}` notation
- **Expected value**: `E[r_i]` notation

### HTML Styling with Tailwind CSS
- **Professional layout**: Responsive design with proper margins and spacing
- **Color coding**: Blue headers, red section titles, bold cue columns
- **Table formatting**: Clean tables with borders, proper cell padding, responsive design
- **Typography**: Modern font styling for different content types
- **Accessibility**: Semantic HTML structure

## Usage Examples

### Command Line Interface
```bash
# Basic conversion
python cornell_html_converter.py notes.md

# Custom output filename
python cornell_html_converter.py notes.md -o "finance_notes.html"
```

### Python Module Usage
```python
from cornell_html_converter import CornellNotesHTMLConverter

# Convert existing file
converter = CornellNotesHTMLConverter("output.html")
converter.convert_file("notes.md")

# Convert text directly
converter.convert_text(markdown_string)
```

## Input Format Requirements

### Cornell Table Structure
```markdown
### Cue Column | Notes Section
---|---
**Question 1?** | • Detailed answer here
**What is alpha?** | • α measures manager skill
**CAPM equation?** | • $r_{i,t} - r_{F,t} = \alpha_i + \beta_i(r_{M,t} - r_{F,t}) + \varepsilon_{i,t}$
```

### Section Organization
```markdown
# Main Title
## Section Name
---
### Cue Column | Notes Section
[table content]
---
## Summary
Summary paragraph content here.
```

## Dependencies

```
markdown>=3.4.0
```

Install with: `pip install markdown`

Note: Tailwind CSS and MathJax are loaded via CDN in the HTML output.

## Technical Implementation Details

### Core Classes
- **CornellNotesHTMLConverter**: Main converter class
  - `__init__(output_filename)`: Initialize converter
  - `convert_file(input_file)`: Convert markdown file to HTML
  - `convert_text(markdown_text)`: Convert text string to HTML
  - `get_html_template()`: Return HTML template with Tailwind CSS and MathJax
  - `preserve_latex_for_html(text)`: Preserve LaTeX for MathJax rendering
  - `parse_cornell_table(content)`: Extract cue/notes pairs
  - `process_markdown_content(content)`: Main parsing logic
  - `create_cornell_table_html(pairs)`: Generate HTML table

### LaTeX Processing Pipeline
1. **Preservation**: LaTeX expressions are preserved for MathJax
2. **HTML escaping**: Non-math content is properly HTML-escaped
3. **MathJax rendering**: Client-side rendering of mathematical expressions

### HTML Generation Pipeline
1. **Content parsing**: Extract sections, tables, equations
2. **HTML generation**: Create semantic HTML with Tailwind classes
3. **Template insertion**: Insert content into HTML template
4. **File output**: Write complete HTML document

## Sample Input/Output

### Input (Markdown)
```markdown
# Active Money Management Notes

## CAPM Framework
---

### Cue Column | Notes Section
---|---
**What is alpha?** | • $\alpha_i$ = manager skill beyond market risk
**CAPM equation?** | • $r_{i,t} - r_{F,t} = \alpha_i + \beta_i(r_{M,t} - r_{F,t}) + \varepsilon_{i,t}$

---

## Summary
CAPM separates returns into risk-free rate, market risk premium, and alpha.
```

### Output Features
- Professional HTML with responsive Cornell note layout
- Mathematical equations rendered with MathJax
- Tailwind CSS styling with modern design
- Clean table formatting with proper responsive behavior
- Semantic HTML structure for accessibility

## Potential Extensions

### Enhancement Opportunities
1. **Dark Mode Support**: Toggle between light and dark themes
2. **Print Styles**: CSS optimized for printing
3. **Export Options**: PDF generation from HTML, Word export
4. **Interactive Features**: Collapsible sections, search functionality
5. **Custom Themes**: User-configurable color schemes
6. **Progressive Web App**: Offline capability and mobile app features

### Current Advantages over PDF
1. **Responsive Design**: Works on all screen sizes
2. **Interactive Math**: Copy/paste LaTeX equations
3. **Searchable Content**: Browser search works on all content
4. **Accessibility**: Screen reader compatible
5. **Web Integration**: Easy to embed or share online
6. **Modern Styling**: Tailwind CSS provides contemporary look

## Error Handling

The script includes error handling for:
- File not found errors
- Malformed markdown content
- LaTeX parsing issues
- HTML generation failures

## Testing Recommendations

When extending this code, test with:
1. **Various LaTeX expressions**: Greek letters, complex equations
2. **Different note structures**: Multiple sections, long content
3. **Edge cases**: Empty sections, malformed tables
4. **Large documents**: Performance with extensive notes
5. **Mobile devices**: Responsive behavior on different screen sizes

## Integration Notes

This converter was designed to be:
- **Modular**: Easy to import and use in other projects
- **Extensible**: Clear separation of concerns for easy modification
- **Web-friendly**: Generates standards-compliant HTML
- **Modern**: Uses current web technologies (Tailwind CSS, MathJax)

The code follows Python best practices and can be easily integrated into larger note-taking, learning management systems, or documentation platforms.