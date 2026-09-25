import re
import os

with open('Presentacion_Escritura_Reflexiva.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# find all sections
pattern = re.compile(r'<section\s+([^>]*?)>(.*?)</section>', re.DOTALL)
matches = pattern.findall(content)
print(f"Total sections found: {len(matches)}")

for idx in range(len(matches)):
    attrs, body = matches[idx]
    id_m = re.search(r'id=["\']([^"\']+)["\']', attrs)
    sid = id_m.group(1) if id_m else f'slide-{idx+1}'
    h_m = re.search(r'<h[1-4][^>]*>(.*?)</h[1-4]>', body, re.DOTALL)
    htext = re.sub(r'<[^>]+>', '', h_m.group(1)).strip() if h_m else 'Sin encabezado'
    imgs = re.findall(r'<img\s+[^>]*?>', body)
    print(f"--- Slide {idx+1:02d} [{sid}]: {htext[:45]} ---")
    for img in imgs:
        alt_m = re.search(r'alt=["\']([^"\']+)["\']', img)
        alt = alt_m.group(1) if alt_m else 'NO ALT'
        src_m = re.search(r'src=["\']([^"\']+)["\']', img)
        src = src_m.group(1) if src_m else ''
        print(f"   IMG: {alt} (src starts: {src[:30]}, len: {len(src)})")
