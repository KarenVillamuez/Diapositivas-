import urllib.request, json, urllib.parse

headers = {'User-Agent': 'AcademicPresentationBot/1.0 (colmayor_cartagena2026@colmayor.edu.co)'}

def search_and_download(q, dest):
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': q,
        'srnamespace': '6',
        'srlimit': '10',
        'format': 'json'
    }
    url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for item in data.get('query', {}).get('search', []):
            t = item['title']
            if any(t.lower().endswith(x) for x in ['.jpg', '.jpeg', '.png']):
                info_url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode({
                    'action': 'query',
                    'titles': t,
                    'prop': 'imageinfo',
                    'iiprop': 'url',
                    'format': 'json'
                })
                info_req = urllib.request.Request(info_url, headers=headers)
                with urllib.request.urlopen(info_req) as info_resp:
                    info_data = json.loads(info_resp.read().decode('utf-8'))
                    for p in info_data.get('query', {}).get('pages', {}).values():
                        u = p.get('imageinfo', [{}])[0].get('url')
                        if u:
                            print(f'Found {t}: {u}')
                            with urllib.request.urlopen(urllib.request.Request(u, headers=headers)) as r, open(dest, 'wb') as f:
                                f.write(r.read())
                            print('Saved to', dest)
                            return t, u
    return None, None

# 1. USB drive connected to laptop/computer
t1, u1 = search_and_download('USB flash drive connected laptop OR computer', 'assets/real_usb_connected.jpg')
print('USB:', t1, u1)

# 2. Rural students classroom Colombia or Latin America
t2, u2 = search_and_download('rural school classroom students computers Colombia OR "Latin America"', 'assets/real_classroom_students.jpg')
print('Classroom:', t2, u2)
