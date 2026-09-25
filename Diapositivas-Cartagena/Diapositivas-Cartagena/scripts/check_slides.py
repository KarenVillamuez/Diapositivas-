import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find slides by section tag
slides = re.findall(r'<section\s+class="([^"]+)"\s+id="([^"]+)">([\s\S]*?)</section>', text)
for idx, (cls, sid, content) in enumerate(slides, 1):
    cat = re.search(r'class="sh-category">([^<]+)<', content)
    cat_str = cat.group(1).strip() if cat else ''
    title = re.search(r'<h[1-3][^>]*>([^<]+)<', content)
    title_str = title.group(1).strip() if title else ''
    print(f"Slide {idx:02d} [{sid}]: Category = '{cat_str}' | Heading = '{title_str}'")
