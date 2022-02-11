import requests

url='https://httpbin.org/post'

file={"emp.csv":open("emp.csv","rb")}

resp=requests.post(url,files=file)

print(resp.text)