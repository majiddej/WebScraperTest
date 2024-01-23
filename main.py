import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import pandas as pd
from bs4 import BeautifulSoup
from utils import convert_persian_to_english_digits

# edge_options = Options()
# edge_driver_path = 'D:/chromedriver_win32/msedgedriver.exe'
# edge_service = Service(edge_driver_path)
# driver = webdriver.Edge(service=edge_service, options=edge_options)

URL = 'https://www.codal.ir/Reports/Decision.aspx?LetterSerial=RJYb0RsIkbvJqPxlD52BQQQaQQQA%3d%3d&rt=0&let=58&ct=0&ft=-1'
# driver.get(URL)
# Allow JavaScript to execute (wait for some time to load)
# driver.implicitly_wait(15000)

# Get the page source after JavaScript execution
# html_content = driver.page_source
# Don't forget to close the Selenium webdriver when you're done
# driver.quit()
# URL = "https://www.cbi.ir/Inflation/Inflation_FA.aspx"
html_content = requests.get(URL, verify=False)
print(f"status code: {html_content.status_code}")
soup = BeautifulSoup(html_content.text, 'html.parser')

print(soup.prettify())
