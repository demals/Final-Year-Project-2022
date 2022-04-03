from urllib import response
import requests, http_checker

headers = {'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'}
url = input()
url = http_checker.http_check(url)
try:
    r = requests.get(url, allow_redirects=False, headers=headers)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
print(r.status_code)
print(url)
print(r.next.url)