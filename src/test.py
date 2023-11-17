import requests
from pyquery import PyQuery as pq
import time
from utils import sys_config, get_logger

# use config
configs = sys_config()
print(configs["login"]["user"])

response = requests.get(url="https://koto-hsc3.revn.jp/auth/login")
doc = pq(response.content.decode("utf-8"))
_Token_fields = doc("input[name='_Token[fields]']")
print("_Token_fields:", _Token_fields[0].get("value"))

csrfToken = response.cookies.get("csrfToken")
usersessid = response.cookies.get("USERSESSID")
print(csrfToken)
print(usersessid)
_csrfToken = doc("input[name='_csrfToken']")
print("csrfToken:", _csrfToken[0].get("value"))

time.sleep(1)

body = {
    "_csrfToken": _csrfToken[0].get("value"),
    "login_id": configs["login"]["user"],
    "password": configs["login"]["password"],
    "_Token[fields]": _Token_fields[0].get("value"),
    "_Token[unlocked]": "",
}
cookie = "csrfToken=" + csrfToken + "; USERSESSID=" + usersessid
header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Cookie": cookie,
}

response_login = requests.post(url=configs["login"]["url"], data=body, headers=header)
print(response_login)

response_mypage = requests.get(
    url="https://koto-hsc3.revn.jp/user/detail/18995", headers=header
)
print(response_mypage.content.decode("utf-8"))
