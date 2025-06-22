# Cornell Notes HTML Converter

A Python script that converts Cornell-style notes written in Markdown format to beautiful, responsive HTML documents with professional styling using Tailwind CSS and MathJax for mathematical equations.

![Cornell Notes HTML Converter](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-38B2AC.svg)
![MathJax](https://img.shields.io/badge/MathJax-3.0-orange.svg)

## ✨ Features

- **🎓 Cornell Note Format**: Authentic two-column layout (cue column | notes section)
- **🧮 LaTeX Math Support**: Full mathematical equation rendering with MathJax
- **🎨 Beautiful Design**: Professional styling with Tailwind CSS
- **📱 Responsive Layout**: Works perfectly on desktop, tablet, and mobile
- **⚡ Fast & Lightweight**: No heavy dependencies, loads quickly
- **🔧 Easy to Use**: Simple command-line interface

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Input Format](#input-format)
- [Examples](#examples)
- [Features in Detail](#features-in-detail)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- `pip` package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Dependencies

- `markdown>=3.4.0` - For Markdown processing
- Tailwind CSS and MathJax are loaded via CDN (no local installation required)

## 💻 Usage

### Command Line Interface

```bash
# Basic conversion
python cornell_html_converter.py notes.md

# Custom output filename
python cornell_html_converter.py notes.md -o my_notes.html

# View help
python cornell_html_converter.py --help
```

### Python Module Usage

```python
from cornell_html_converter import CornellNotesHTMLConverter

# Convert a file
converter = CornellNotesHTMLConverter("output.html")
converter.convert_file("notes.md")

# Convert text directly
markdown_text = """
# My Notes
## Section 1
### Cue | Notes
**Question?** | Answer here
"""
converter.convert_text(markdown_text)
```

## 📝 Input Format

### Cornell Table Structure

Use this format for Cornell-style two-column notes:

```markdown
### Cue Column | Notes Section
---|---
**What is X?** | • Definition of X
**Key Formula?** | • $E = mc^2$
**Important Point** | • First point
 | • Second point (continuation)
```

### Complete Document Structure

```markdown
# Document Title

## Section Name
---

### Cue Column | Notes Section
---|---
**Question 1?** | • Answer with details
**Question 2?** | • Mathematical formula: $\alpha = \beta + \gamma$
**Complex Topic** | • Multiple bullet points
 | • Can span multiple lines
 | • $\frac{d}{dx}f(x) = f'(x)$

---

## Summary

Your summary paragraph here with LaTeX support: $\sum_{i=1}^{n} x_i$.
```

### LaTeX Math Support

The converter supports full LaTeX mathematical notation:

```markdown
Inline math: $\alpha + \beta = \gamma$
Block math: $$\int_{0}^{\infty} e^{-x} dx = 1$$
Greek letters: $\alpha, \beta, \gamma, \delta, \pi, \sigma$
Fractions: $\frac{a}{b}$
Subscripts/Superscripts: $x_{i,j}^{2}$
```

## 🎯 Examples

### Academic Finance Notes

```markdown
# Portfolio Theory

## CAPM Framework
---

### Cue Column | Notes Section
---|---
**What is alpha?** | • $\alpha_i$ measures manager skill beyond market risk
 | • Positive alpha indicates outperformance
**CAPM Equation** | • $r_{i,t} - r_{F,t} = \alpha_i + \beta_i(r_{M,t} - r_{F,t}) + \varepsilon_{i,t}$
**Beta Definition** | • $\beta_i = \frac{Cov(r_i, r_M)}{Var(r_M)}$
 | • Measures systematic risk exposure

---

## Summary
The CAPM framework separates returns into systematic risk ($\beta$) and 
manager skill ($\alpha$), providing a foundation for performance evaluation.
```

### Study Notes Template

```markdown
# Course Name - Chapter X

## Key Concepts
---

### Cue Column | Notes Section
---|---
**Definition** | • Clear, concise definition
**Formula** | • $y = mx + b$
**Example** | • Step-by-step example
**Why Important?** | • Practical applications
 | • Real-world relevance

---

## Summary
Chapter summary with main takeaways and connections to other topics.
```

## 🎨 Features in Detail

### Professional Styling

- **Modern Design**: Clean, professional appearance with Tailwind CSS
- **Color Coding**: 
  - Blue accents for titles and highlights
  - Red section headers for clear organization
  - Gray cue columns with blue left borders
  - Gradient backgrounds for visual appeal

### Cornell Note Layout

- **Authentic Format**: True to traditional Cornell note-taking methodology
- **30/70 Split**: Optimal cue column to notes column ratio
- **Visual Separation**: Clear borders and background distinctions
- **Consistent Spacing**: Professional typography and spacing

### Mathematical Equations

- **MathJax Integration**: Industry-standard math rendering
- **Full LaTeX Support**: All mathematical notation supported
- **Responsive Math**: Equations scale properly on all devices
- **Copy/Paste Friendly**: Users can copy LaTeX source

### Responsive Design

- **Mobile Optimized**: Tables and content adapt to small screens
- **Tablet Friendly**: Optimal viewing on medium-sized devices
- **Desktop Perfect**: Full-width layout on large screens
- **Print Ready**: Clean printing with proper page breaks

## 🛠 Customization

### Styling Customization

The converter includes CSS custom properties that can be modified:

```css
.cornell-cue {
    background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
    border-right: 3px solid #3b82f6;
}

.cornell-notes {
    background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
}
```

### Extending the Converter

You can extend the `CornellNotesHTMLConverter` class:

```python
class CustomCornellConverter(CornellNotesHTMLConverter):
    def get_html_template(self):
        # Return your custom template
        return custom_template
        
    def create_cornell_table_html(self, pairs):
        # Custom table generation
        super().create_cornell_table_html(pairs)
```

## 📊 Output Features

The generated HTML includes:

- ✅ **Semantic HTML5** structure for accessibility
- ✅ **Responsive design** with Tailwind CSS
- ✅ **Mathematical equations** rendered with MathJax
- ✅ **Professional typography** with Google Fonts (Inter)
- ✅ **Print-optimized** CSS for hard copies
- ✅ **SEO-friendly** document structure
- ✅ **Fast loading** with CDN resources

## 🔧 Troubleshooting

### Common Issues

**Math not rendering:**
- Ensure proper LaTeX syntax: `$math$` for inline, `$$math$$` for block
- Check that MathJax is loading (requires internet connection)

**Table not formatting:**
- Verify the table header: `### Cue Column | Notes Section`
- Include the separator line: `---|---`
- Check for proper pipe `|` separators

**Missing styles:**
- Ensure internet connection for Tailwind CSS CDN
- Check that HTML file is opened in a modern browser

### Performance Tips

- Large documents may take a moment to render math equations
- For offline use, consider downloading Tailwind CSS and MathJax locally
- Use smaller images if embedding pictures in notes

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature-name`
3. **Make your changes** and add tests
4. **Submit a pull request** with a clear description

### Development Setup

```bash
git clone https://github.com/your-username/cornell-notes-html-converter.git
cd cornell-notes-html-converter
pip install -r requirements.txt
python cornell_html_converter.py sample_notes.md
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

- **Issues**: Report bugs or request features via GitHub Issues
- **Documentation**: Check the [CONTEXT.md](CONTEXT.md) file for technical details
- **Examples**: See the included `sample_notes.md` for formatting examples

## 🎯 Roadmap

Future enhancements planned:

- [ ] **Dark mode toggle**
- [ ] **Custom color themes**
- [ ] **PDF export functionality**
- [ ] **Interactive features** (collapsible sections)
- [ ] **Search functionality**
- [ ] **Table of contents generation**
- [ ] **Note linking and cross-references**

## 🏆 Why Cornell Notes?

The Cornell Note-taking System, developed at Cornell University, is a systematic format for condensing and organizing notes. This converter brings this proven methodology to the digital age with:

- **Structured Learning**: Forces active engagement with material
- **Review Friendly**: Easy to scan and review key concepts
- **Study Efficient**: Separates questions from answers for self-testing
- **Professional Appearance**: Clean, organized presentation

---

**Made with ❤️ for students, researchers, and lifelong learners**