import urllib.request
import re
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# 1. Search for College ESL Writers
for i in range(1, 20):
    url = f"https://oer.galileo.usg.edu/english-textbooks/{i}/"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=4) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            if 'College ESL Writers' in html:
                m = re.search(r'property="og:image"\s+content="([^"]+)"', html)
                img = m.group(1) if m else "No og:image"
                print(f"Book found at {url}: {img}")
                # Download cover image
                if img != "No og:image":
                    urllib.request.urlretrieve(img, "assets/real_book_college_esl.jpg")
                    print("Saved assets/real_book_college_esl.jpg")
                break
    except Exception as e:
        continue

# 2. Search Wikimedia Commons for real Colombian rural school computers
commons_api = "https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch=rural+school+Colombia+OR+Computadores+para+Educar&gsrlimit=10&prop=imageinfo&iiprop=url|extmetadata&format=json"
try:
    req = urllib.request.Request(commons_api, headers=headers)
    with urllib.request.urlopen(req, timeout=5) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        pages = data.get('query', {}).get('pages', {})
        for pid, pinfo in pages.items():
            title = pinfo.get('title')
            ii = pinfo.get('imageinfo', [{}])[0]
            url = ii.get('url')
            desc = ii.get('extmetadata', {}).get('ImageDescription', {}).get('value', '')
            print(f"Commons file: {title} -> {url}")
except Exception as e:
    print(f"Commons error: {e}")

# 3. Search Wikimedia Commons for USB flash drive in computer
commons_usb = "https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6&gsrsearch=USB+flash+drive+computer+port+plugged&gsrlimit=5&prop=imageinfo&iiprop=url&format=json"
try:
    req = urllib.request.Request(commons_usb, headers=headers)
    with urllib.request.urlopen(req, timeout=5) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        pages = data.get('query', {}).get('pages', {})
        for pid, pinfo in pages.items():
            title = pinfo.get('title')
            url = pinfo.get('imageinfo', [{}])[0].get('url')
            print(f"Commons USB: {title} -> {url}")
except Exception as e:
    print(f"Commons USB error: {e}")
