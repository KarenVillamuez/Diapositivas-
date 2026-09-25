import re
import os

with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
print(f"Total img tags: {len(imgs)}")
unique_imgs = set(imgs)
all_ok = True
for img in sorted(unique_imgs):
    clean_path = img.split('?')[0]
    exists = os.path.exists(clean_path)
    size = os.path.getsize(clean_path) if exists else 0
    status = "OK" if exists else "MISSING"
    print(f"  [{status}] {clean_path}: size={size} bytes")
    if not exists:
        all_ok = False

if all_ok:
    print("\nALL ASSETS EXIST AND ARE VALID!")
else:
    print("\nWARNING: SOME ASSETS ARE MISSING!")
