from urllib.request import Request,urlopen,build_opener,HTTPCookieProcessor
from http.cookiejar import CookieJar
import requests
header={"User-Agent": "Mozilla/5.0",}
cookies={'name':'rika'}
# Request("https://www.google.co.in/",headers=header)
resp=requests.post("https://www.google.co.in/",cookies=cookies,headers=header)
# print(resp.headers)
# print(dir(resp))
print(resp.text)
# print(resp.headers)
print(resp.cookies)

# print(type(resp.headers))

# for val in resp.headers:
#     print(val)

# opener=build_opener(HTTPCookieProcessor(cookie_jar))

# opener.open("https://www.google.co.in/")

# cookie_jar_list=list(cookie_jar)

# for val in cookie_jar:
#     print(val)


# print(len(cookie_jar))


