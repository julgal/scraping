import requests
from bs4 import BeautifulSoup

url = ""
#HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

response = requests.get(url)
response.encoding = response.apparent_encoding

data = []

if response.status_code == 200:
	html = response.text

	f = open("file.html", "w")
	f.write(html)
	f.close()

	soup = BeautifulSoup(html, "html5lib")

else:
	print("Erreur :", response.status_code)

