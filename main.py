import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

static_url = "https://jsonplaceholder.typicode.com/todos/"
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

results = []

for number in numbers:
    api_url = f"{static_url}{number}"
    driver.get(api_url)
    time.sleep(1)
    page_source = driver.page_source

    if page_source.startswith("<html>"):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        page_source = soup.get_text()
    try:
        data = json.loads(page_source)
        results.append(f"{api_url} - Data in JSON format.")
    except json.JSONDecodeError:
        results.append(f"{api_url} - Data can be string, not in JSON format.")

driver.quit()

for result in results:
    print(result)




