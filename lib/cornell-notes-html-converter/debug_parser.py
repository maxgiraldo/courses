#!/usr/bin/env python3

import re

def clean_latex_for_pdf(text: str) -> str:
    """Debug version of LaTeX cleaning"""
    # Greek letters mapping
    greek_letters = {
        r'\\alpha': 'α', r'\\beta': 'β', r'\\gamma': 'γ', r'\\delta': 'δ',
        r'\\epsilon': 'ε', r'\\varepsilon': 'ε', r'\\sigma': 'σ', r'\\mu': 'μ'
    }
    
    def process_inline_math(match):
        math_content = match.group(1)
        
        # Apply Greek letters
        for latex, unicode_char in greek_letters.items():
            math_content = re.sub(latex, unicode_char, math_content)
        
        # Handle subscripts r_{i,t} -> r[i,t]
        math_content = re.sub(r'([a-zA-Z])_\{([^}]+)\}', r'\1[\2]', math_content)
        math_content = re.sub(r'([a-zA-Z])_([a-zA-Z0-9])', r'\1[\2]', math_content)
        
        # Handle fractions \frac{a}{b} -> (a)/(b)
        math_content = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'(\1)/(\2)', math_content)
        
        return math_content
    
    # Process inline math $...$
    text = re.sub(r'\$([^$]+)\$', process_inline_math, text)
    return text

def parse_cornell_table_debug(content: str):
    """Debug version of Cornell table parsing."""
    print("=== DEBUG: Parsing table content ===")
    print(f"Content:\n{content}")
    print("=" * 40)
    
    lines = content.strip().split('\n')
    pairs = []
    current_cue = ""
    current_notes = []
    
    for i, line in enumerate(lines):
        print(f"Line {i}: '{line}'")
        
        if '|' in line and not line.strip().startswith('---'):
            parts = line.split('|', 1)
            if len(parts) == 2:
                cue_part = parts[0].strip()
                notes_part = parts[1].strip()
                
                print(f"  Cue: '{cue_part}'")
                print(f"  Notes: '{notes_part}'")
                
                # If we have a new cue (not empty), save previous pair and start new one
                if cue_part:
                    # Save previous pair if exists
                    if current_cue and current_notes:
                        clean_cue = re.sub(r'\*\*(.*?)\*\*', r'\1', current_cue)
                        clean_cue = clean_latex_for_pdf(clean_cue)
                        clean_notes = clean_latex_for_pdf(' '.join(current_notes))
                        pairs.append((clean_cue, clean_notes))
                        print(f"  SAVED PAIR: '{clean_cue}' -> '{clean_notes}'")
                    
                    # Start new pair
                    current_cue = cue_part
                    current_notes = [notes_part] if notes_part else []
                    print(f"  NEW CUE: '{current_cue}'")
                else:
                    # Continuation of previous notes (empty cue column)
                    if notes_part:
                        current_notes.append(notes_part)
                        print(f"  ADDED TO NOTES: '{notes_part}'")
    
    # Don't forget the last pair
    if current_cue and current_notes:
        clean_cue = re.sub(r'\*\*(.*?)\*\*', r'\1', current_cue)
        clean_cue = clean_latex_for_pdf(clean_cue)
        clean_notes = clean_latex_for_pdf(' '.join(current_notes))
        pairs.append((clean_cue, clean_notes))
        print(f"  FINAL PAIR: '{clean_cue}' -> '{clean_notes}'")
    
    print(f"\nFINAL PAIRS ({len(pairs)}):")
    for i, (cue, notes) in enumerate(pairs):
        print(f"{i+1}. CUE: '{cue}'")
        print(f"   NOTES: '{notes}'")
    
    return pairs

# Test with sample content
sample_table = """**What is alpha?** | • $\\alpha_i$ = manager skill beyond market risk
 | • Measures excess return after adjusting for systematic risk
 | • Positive alpha indicates outperformance
**CAPM equation?** | • $r_{i,t} - r_{F,t} = \\alpha_i + \\beta_i(r_{M,t} - r_{F,t}) + \\varepsilon_{i,t}$
 | • $r_i$ = return on asset i, $r_F$ = risk-free rate
 | • $r_M$ = market return, $\\beta_i$ = systematic risk"""

if __name__ == "__main__":
    parse_cornell_table_debug(sample_table)