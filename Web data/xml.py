import urllib

url="http://httpbin.org/xml"
result=urllib.request.urlopen(url)
print("Status code: ",result.status)
print("\n Headers: ",result.headers())