import requests
from pyquery import PyQuery as pq

response = requests.get(url='https://koto-hsc3.revn.jp/auth/login')
doc = pq(response.content.decode('utf-8'))
_csrfToken = doc('input[name=_csrfToken]')
#print(_csrfToken)

cookie = response.cookies
print(cookie.get('csrfToken'))