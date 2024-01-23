import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import pandas as pd
from bs4 import BeautifulSoup

from utils import convert_persian_to_english_digits

persion_number = '-.-'
english_number = float(convert_persian_to_english_digits(persion_number))

edge_options = Options()
edge_driver_path = 'D:/chromedriver_win32/msedgedriver.exe'
edge_service = Service(edge_driver_path)

driver = webdriver.Edge(service=edge_service, options=edge_options)

url = 'https://www.cbi.ir/Inflation/Inflation_FA.aspx'
driver.get(url)
# Allow JavaScript to execute (wait for some time to load)
driver.implicitly_wait(15000)

# Get the page source after JavaScript execution
html_content = driver.page_source
# Don't forget to close the Selenium webdriver when you're done
driver.quit()
# URL = "https://www.cbi.ir/Inflation/Inflation_FA.aspx"
# r = requests.get(URL,verify=False)

soup = BeautifulSoup(html_content, 'html5lib')

# Find the tables using their class attribute or any other identifying feature
monthly_table = soup.find('table', class_='table table-hover table-responsive table-condensed table-bordered table-striped')
annual_table = soup.find_all('table', class_='table table-hover table-responsive table-condensed table-bordered table-striped')[1]

# Extract data from the monthly table
monthly_data = []
for row in monthly_table.find_all('tr')[1:]:
    columns = row.find_all('td')
    month = columns[0].text.strip()
    index = columns[1].text.strip()
    inflation_rate = columns[2].text.strip()
    monthly_data.append({'Month': month, 'Index': index, 'Inflation Rate': inflation_rate})

# Extract data from the annual table
annual_data = []
for row in annual_table.find_all('tr')[1:]:
    columns = row.find_all('td')
    year = columns[0].text.strip()
    index = columns[1].text.strip()
    inflation_rate = columns[2].text.strip()
    annual_data.append({'Year': year, 'Index': index, 'Inflation Rate': inflation_rate})

# Print the extracted data
print("Monthly Data:")
for data in monthly_data:
    print(data)

print("\nAnnual Data:")
for data in annual_data:
    print(data)


# Save data to Excel file in separate sheets
excel_file_path = 'D:/output_file.xlsx'
# Create DataFrames from the extracted tables
monthly_data_df = pd.DataFrame(monthly_data)
annual_data_df = pd.DataFrame(annual_data)
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    monthly_data_df.to_excel(writer, sheet_name='Monthly Data', index=False)
    annual_data_df.to_excel(writer, sheet_name='Annual Data', index=False)

