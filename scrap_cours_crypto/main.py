# pip install beautifulsoup4
# pip install html5li"utf-8"b
import requests
from bs4 import BeautifulSoup
from formated_data import remove_duplicate_lines
from formated_data import clean_up_files
from formated_data import check_file_exists

url = "https://courscryptomonnaies.com/"

def get_data():
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    if response.status_code == 200:
        html = response.text
        with open("cours.html", "w") as file:
            file.write(html)
            #print(html)
    else:
        print(f"Error: {response.status_code}")


def file_processing():
    with open("cours.html", "r") as file: 
        soup = BeautifulSoup(file, "html5lib")
        title = soup.find("h1").text
        span = soup.find_all(class_="jsx-1338272632")
    with open("data.txt", "w") as file:
        for crypto in span:
            file.write(crypto.get_text())
            file.write("\n")


if __name__ == "__main__":
    get_data()
    file_processing()
    remove_duplicate_lines("data.txt", "new_data.txt")
    clean_up_files()

