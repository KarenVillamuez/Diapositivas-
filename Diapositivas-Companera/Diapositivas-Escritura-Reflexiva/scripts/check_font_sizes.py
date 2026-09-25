import os, glob, re

slide_files = sorted(glob.glob('slides/slide_*.html'))
small_fonts = []

for sf in slide_files:
    with open(sf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = re.findall(r'font-size:\s*(\d+)px', content)
    for m in matches:
        val = int(m)
        if val < 18:
            small_fonts.append((sf, val))

print(f"Total small font occurrences (< 18px): {len(small_fonts)}")
for sf, val in small_fonts[:30]:
    print(f"  {sf}: {val}px")
