from bs4 import BeautifulSoup

with open('file.html') as fp:
	soup = BeautifulSoup(fp, "html5lib")

html = soup.find_all("")
data = []

for h in html:
	data.append(h.text)
