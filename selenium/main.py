from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = ''
driver.get(url)

sleep(4)

data_emails = []

def get_data():
    emails = driver.find_elements(By.XPATH, '//li[@class="mail"]//a')
    
    for email in emails:
        data_emails.append(email.text)
        print(email.text)

def click_next_page():
    next_page = driver.find_element(By.XPATH, '//li[@class="pager-next"]//a')
    driver.execute_script("arguments[0].click();", next_page)

get_data()
sleep(2)

for _ in range(5):
    click_next_page()
    sleep(2)
    get_data()

driver.quit()
for d in data_emails:
    print(data_emails[d])