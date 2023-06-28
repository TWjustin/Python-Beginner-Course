import requests
url = 'https://www.google.com.tw/?hl=zh_TW'
r = requests.get(url)
if r.status_code == requests.codes.ok:
    print(r.text)