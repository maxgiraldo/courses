# Cornell Notes PDF Converter Project

## Project Overview

This project provides a Python script that converts Cornell-style notes written in markdown format to professionally formatted PDF documents. The converter was specifically designed to handle academic finance notes with LaTeX mathematical equations.

## Background & Use Case

The original use case involved converting Active Money Management course notes that included:
- Cornell note-taking format (cue column | notes section)
- CAPM equations and financial formulas in LaTeX
- Complex mathematical notation (Greek letters, subscripts, superscripts)
- Multiple sections with summaries

## File Structure

```
project/
├── cornell_pdf_converter.py    # Main conversion script
├── CONTEXT.md                 # This documentation file
├── sample_notes.md            # Example Cornell notes (finance/CAPM)
└── requirements.txt           # Python dependencies
```

## Key Features Implemented

### Cornell Note Format Support
- **Two-column layout**: Cue column (questions/keywords) | Notes column (detailed content)
- **Section headers**: Automatic formatting of `## Section Name`
- **Summary sections**: Special formatting for summary content
- **Page breaks**: Support for `---` horizontal rules

### LaTeX Math Processing
- **Inline math**: `$equation$` notation
- **Block equations**: `$$equation$$` notation
- **Greek letters**: α, β, γ, ε, σ, μ, π, Δ, etc.
- **Mathematical symbols**: ±, ×, ÷, ≤, ≥, ≠, ≈, →, ⇒
- **Subscripts/Superscripts**: `r_{i,t}`, `x^2` formatting
- **Fractions**: `\frac{a}{b}` → `(a)/(b)`
- **Expected value**: `E[r_i]` notation

### PDF Styling
- **Professional layout**: Proper margins, spacing, typography
- **Color coding**: Blue headers, red section titles, bold cue columns
- **Table formatting**: Grid lines, proper cell padding, column sizing
- **Typography**: Multiple font styles for different content types

## Usage Examples

### Command Line Interface
```bash
# Basic conversion
python cornell_pdf_converter.py notes.md

# Custom output filename
python cornell_pdf_converter.py notes.md -o "finance_notes.pdf"

# A4 page size (default is US Letter)
python cornell_pdf_converter.py notes.md --page-size a4
```

### Python Module Usage
```python
from cornell_pdf_converter import CornellNotesPDFConverter

# Convert existing file
converter = CornellNotesPDFConverter("output.pdf")
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
reportlab>=3.6.0
markdown>=3.4.0
html2text>=2020.1.16
```

Install with: `pip install reportlab markdown html2text`

## Technical Implementation Details

### Core Classes
- **CornellNotesPDFConverter**: Main converter class
  - `__init__(output_filename, page_size)`: Initialize converter
  - `convert_file(input_file)`: Convert markdown file to PDF
  - `convert_text(markdown_text)`: Convert text string to PDF
  - `setup_custom_styles()`: Define PDF typography styles
  - `clean_latex_for_pdf(text)`: Convert LaTeX to Unicode
  - `parse_cornell_table(content)`: Extract cue/notes pairs
  - `process_markdown_content(content)`: Main parsing logic

### LaTeX Processing Pipeline
1. **Pattern matching**: Regex to find `$...$` and `$$...$$`
2. **Symbol conversion**: LaTeX commands → Unicode characters
3. **Structure handling**: Subscripts, superscripts, fractions
4. **Formatting preservation**: Maintain mathematical meaning

### PDF Generation Pipeline
1. **Content parsing**: Extract sections, tables, equations
2. **Style application**: Apply appropriate formatting
3. **Layout creation**: Two-column tables, proper spacing
4. **Document assembly**: Build final PDF with ReportLab

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
- Professional PDF with proper Cornell note layout
- Mathematical equations rendered clearly
- Color-coded sections and bold cue column
- Clean table formatting with grid lines

## Potential Extensions

### Enhancement Opportunities
1. **Enhanced Math Support**: More LaTeX commands, matrix notation
2. **Image Support**: Embedded charts, diagrams, figures
3. **Custom Styling**: User-configurable colors, fonts, layouts
4. **Export Formats**: HTML, Word, LaTeX output options
5. **Interactive Features**: Clickable table of contents, cross-references
6. **Mobile Optimization**: Responsive layouts for different devices

### Known Limitations
1. **Complex LaTeX**: Advanced mathematical notation may not convert perfectly
2. **Image Handling**: No support for embedded images currently
3. **Table Complexity**: Only supports basic two-column Cornell format
4. **Font Limitations**: Limited mathematical symbol support in ReportLab

## Error Handling

The script includes error handling for:
- File not found errors
- Malformed markdown content
- LaTeX parsing issues
- PDF generation failures

## Testing Recommendations

When extending this code, test with:
1. **Various LaTeX expressions**: Greek letters, complex equations
2. **Different note structures**: Multiple sections, long content
3. **Edge cases**: Empty sections, malformed tables
4. **Large documents**: Performance with extensive notes

## Integration Notes

This converter was designed to be:
- **Modular**: Easy to import and use in other projects
- **Extensible**: Clear separation of concerns for easy modification
- **Robust**: Handles edge cases and provides error feedback
- **Standards-compliant**: Uses established libraries (ReportLab, Markdown)

The code follows Python best practices and can be easily integrated into larger note-taking or document processing systems.