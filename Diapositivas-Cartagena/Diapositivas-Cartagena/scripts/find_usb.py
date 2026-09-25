import urllib.request, json, urllib.parse

headers = {'User-Agent': 'AcademicPresentationBot/1.0 (colmayor_cartagena2026@colmayor.edu.co)'}

def get_url(title):
    info_params = {
        'action': 'query',
        'titles': title,
        'prop': 'imageinfo',
        'iiprop': 'url',
        'format': 'json'
    }
    info_url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(info_params)
    req = urllib.request.Request(info_url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for p in data.get('query', {}).get('pages', {}).values():
            return p.get('imageinfo', [{}])[0].get('url')

params = {
    'action': 'query',
    'list': 'search',
    'srsearch': 'USB flash drive laptop OR computer filetype:bitmap',
    'srnamespace': '6',
    'srlimit': '15',
    'format': 'json'
}
url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(params)
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    for item in data.get('query', {}).get('search', []):
        t = item['title']
        if any(t.lower().endswith(x) for x in ['.jpg', '.jpeg', '.png']):
            img_url = get_url(t)
            print(f"{t} -> {img_url}")
