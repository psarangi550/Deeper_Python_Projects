from http.cookiejar import CookieJar
from urllib.request import urlopen,build_opener,HTTPCookieProcessor

# cookie_jar=CookieJar() #creating the object of cookie jar

opener = build_opener()

opener.addheaders.append(name='rika')

# opener.addheaders.append('Cookie','name=rika')

opener.open("https://www.google.co.in/")

cookies=list(cookie_jar)

print(len(cookie_jar))

print(cookies)