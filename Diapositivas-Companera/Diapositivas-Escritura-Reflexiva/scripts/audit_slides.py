import glob
import os
import re

slides = sorted(glob.glob('slides/slide_*.html'))
print(f"Total slides found: {len(slides)}")

for s in slides:
    with open(s, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # Check for active box-shadow
    shadows = re.findall(r'box-shadow\s*:\s*([^;]+);', content)
    active_shadows = [sh for sh in shadows if 'none' not in sh.lower()]
    if active_shadows:
        issues.append(f"box-shadow ({len(active_shadows)}: {active_shadows[0].strip()})")
        
    # Check for active border-radius
    radii = re.findall(r'border-radius\s*:\s*([^;]+);', content)
    active_radii = [r for r in radii if r.strip() not in ['0', '0px', 'none']]
    if active_radii:
        issues.append(f"border-radius ({len(active_radii)}: {active_radii[0].strip()})")
        
    # Check for ul / li tags (avoid matching SVG <line>)
    if re.search(r'<(ul|ol|li)\b', content):
        issues.append("has ul/ol/li tags")
        
    # Check for microtext (< 20px)
    px_matches = re.findall(r'font-size\s*:\s*(\d+)px', content)
    micro = [int(p) for p in px_matches if int(p) < 20]
    # Filter badges / mono labels between 14-19px vs true microtext < 14px
    true_micro = [p for p in micro if p < 14]
    if true_micro:
        issues.append(f"severe microtext <14px ({len(true_micro)}: min {min(true_micro)}px)")
    elif micro:
        issues.append(f"sub-badge 14-19px ({len(micro)}: min {min(micro)}px)")
        
    # Check for dark backgrounds on non-separator content slides (containers with padding)
    is_sep = any(num in s for num in ['slide_01', 'slide_03', 'slide_06', 'slide_11', 'slide_18'])
    if not is_sep:
        dark_card_match = re.findall(r'style="[^"]*background(?:-color)?\s*:\s*(#[0-9a-fA-F]{6}|var\(--c-wine-dark\))[^\"]*padding', content)
        forbidden_dark = [bg for bg in dark_card_match if bg.lower() in ['#32060d', '#460811', '#2c0509', 'var(--c-wine-dark)']]
        if forbidden_dark:
            issues.append(f"dark card bg on light slide: {set(forbidden_dark)}")

    status = " | ".join(issues) if issues else "CLEAN"
    print(f"{os.path.basename(s)}: {status}")
