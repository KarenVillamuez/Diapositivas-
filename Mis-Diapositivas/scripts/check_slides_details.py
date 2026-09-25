import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

slides = re.findall(r'<section\s+class="([^"]+)"\s+id="([^"]+)">([\s\S]*?)</section>', text)

for idx, (cls, sid, content) in enumerate(slides, 1):
    print(f"==================== SLIDE {idx:02d} [{sid}] ====================")
    # clean out script/styles/svg if any
    c = re.sub(r'<svg[\s\S]*?</svg>', '[SVG_GRAPH]', content)
    # extract all headers and strong tags or list items
    lines = [l.strip() for l in c.split('\n') if l.strip()]
    meaningful = []
    for l in lines:
        if any(tag in l for tag in ['<h1', '<h2', '<h3', '<h4', '<span class="sh-category"', 'class="s1-', 'class="s2-', 'class="s3-', 'class="s4-', 'class="s16-', 'class="flow-', 'class="bm-', 'class="chart-', 'class="disc-', 'class="ref-', 'class="math-']):
            meaningful.append(re.sub(r'<[^>]+>', ' ', l).strip())
    print('\n'.join(meaningful[:12]))
