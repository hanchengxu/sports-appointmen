import requests

response = requests.get(url='https://koto-hsc3.revn.jp/auth/login')
print(response.status_code)