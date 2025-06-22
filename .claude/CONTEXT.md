# Courses Repository - Project Context

## Repository Overview

This repository contains educational materials, tools, and notes organized into two main areas:
1. **Library tools** (`lib/`) - Reusable utilities and converters
2. **Course materials** (`wharton/`) - Academic course notes and resources

## Project Structure

```
courses/
├── .claude/                              # Claude AI context and configuration
│   └── CONTEXT.md                        # This file - project-level documentation
├── lib/                                  # Reusable library tools and utilities
│   └── cornell-notes-pdf-converter/      # Cornell Notes format converter
│       ├── cornell_pdf_converter.py      # Main converter (HTML output)
│       ├── debug_parser.py              # Development/debugging utilities
│       ├── requirements.txt             # Python dependencies
│       ├── sample_notes.md              # Example Cornell notes format
│       └── CONTEXT.md                   # Library-specific documentation
└── wharton/                             # Wharton School course materials
    └── value-investing/                 # Value Investing course
        └── notes/                       # Course notes directory
            └── 2025-06-22-active-money-management.md
```

## Key Components

### Cornell Notes Converter (`lib/cornell-notes-pdf-converter/`)

**Purpose**: Converts Cornell-style notes from Markdown to HTML format with LaTeX math support.

**Current State**: Recently updated from PDF to HTML generation
- Uses Tailwind CSS for styling
- MathJax for LaTeX equation rendering
- Supports Cornell note format (cue column | notes section)
- Handles mathematical notation in academic content

**Key Features**:
- Two-column Cornell note layout
- LaTeX math expression preservation
- Professional HTML output with responsive design
- Command-line interface for batch processing

**Technical Stack**:
- Python 3.x
- Markdown processing
- HTML generation with Tailwind CSS
- MathJax for mathematical rendering

### Wharton Course Materials (`wharton/`)

**Value Investing Course**:
- Active money management notes
- Financial modeling and analysis
- Academic finance content with mathematical formulas
- Cornell note-taking format for structured learning

## Development Workflow

### Multi-Agent Git Worktree Workflow

For parallel development with multiple AI agents, use git worktrees to isolate work:

**Setup Separate Agent Workspaces**:
```bash
# From main repository directory
cd /Users/max/code/courses

# Create worktrees for different agents/features
git worktree add ../courses-agent1 -b agent1/feature-name
git worktree add ../courses-agent2 -b agent2/feature-name
git worktree add ../courses-agent3 -b agent3/feature-name

# Each agent works in their isolated directory
cd ../courses-agent1  # Agent 1 workspace
cd ../courses-agent2  # Agent 2 workspace
```

**Management Commands**:
```bash
# List all active worktrees
git worktree list

# Remove completed worktrees
git worktree remove ../courses-agent1

# Clean up merged branches
git branch -d agent1/feature-name
```

**Benefits**:
- **Isolation**: Each agent has separate working directory and branch
- **No conflicts**: Agents can't interfere with each other's changes
- **Shared history**: All worktrees share the same `.git` directory
- **Easy switching**: Move between agent workspaces instantly

### Cornell Notes Converter Development

The converter has been evolving from PDF to HTML output:

1. **Original Design**: PDF generation with ReportLab
2. **Current Implementation**: HTML generation with modern web technologies
3. **Key Update**: `CornellNotesHTMLConverter` class replacing PDF functionality

**Recent Changes**:
- Added `create_cornell_table_html()` method for HTML table generation
- Updated `convert_text()` to generate HTML files instead of PDF
- Modified CLI to output `.html` files by default
- Maintained LaTeX math support through MathJax

### File Organization Standards

**Context Documentation**:
- Project-level context in `.claude/CONTEXT.md`
- Component-specific context in respective directories
- Consistent documentation format across components

**Code Organization**:
- Library tools in `lib/` for reusability
- Course-specific materials in domain directories
- Clear separation between utilities and content

## Usage Guidelines

### Cornell Notes Converter

```bash
# Convert markdown notes to HTML
python cornell_pdf_converter.py notes.md

# Specify custom output filename
python cornell_pdf_converter.py notes.md -o finance_notes.html
```

**Input Format**:
```markdown
# Course Title

## Section Name
---

### Cue Column | Notes Section
---|---
**Key Question?** | • Detailed answer with LaTeX: $\alpha = \beta \times r_m$
**Another concept** | • Supporting explanation
                    | • Additional bullet point
```

**Output**: Professional HTML with:
- Responsive Tailwind CSS styling
- MathJax-rendered mathematical equations
- Structured Cornell note layout
- Mobile-friendly design

### Course Notes Organization

**Naming Convention**:
- Date-based naming: `YYYY-MM-DD-topic-name.md`
- Descriptive topic names
- Consistent markdown formatting

**Content Structure**:
- Cornell note format for active learning
- LaTeX math notation for equations
- Clear section organization
- Summary sections for key takeaways

## Integration & Extension

### Library Tools

The Cornell Notes converter is designed as a modular tool:
- Can be imported as a Python module
- Clear API for programmatic usage
- Extensible for additional output formats
- Error handling and validation

### Course Material Integration

Course notes integrate with the converter:
- Standard Cornell format for processing
- LaTeX math notation for complex formulas
- Structured content for easy conversion
- Academic-focused formatting

## Development Environment

**Dependencies**:
- Python 3.x environment
- Markdown processing libraries
- Web-based output (HTML/CSS/JS)
- Mathematical rendering support

**Tools**:
- Git version control
- Python package management
- Web development stack (for HTML output)
- Academic writing tools

## Future Considerations

### Potential Enhancements

1. **Multi-format Output**: PDF, HTML, Word, LaTeX
2. **Enhanced Math Support**: Complex equations, diagrams
3. **Interactive Features**: Searchable content, cross-references
4. **Template System**: Customizable styling and layouts
5. **Batch Processing**: Multiple file conversion workflows
6. **Integration APIs**: LMS integration, note-taking apps

### Scalability

- Modular architecture supports expansion
- Clear separation of concerns
- Reusable components across projects
- Standard interfaces for integration

## Maintenance Notes

**Code Quality**:
- Consistent Python coding standards
- Clear documentation and comments
- Error handling and validation
- Modular design patterns

**Documentation**:
- Keep context files updated with changes
- Document API changes and new features
- Maintain example usage and formats
- Update dependencies and requirements

This repository serves as both a practical tool collection and an educational resource, supporting academic work with professional-quality output formatting.