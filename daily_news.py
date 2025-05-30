from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
import sys
import os
import time

topics = []
descriptions = []
links = []

options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(options=options)
driver.get('https://news.bahai.org/latest')

headlines = driver.find_elements(By.CLASS_NAME , value='root-style-1phzx70')

for headline in headlines:
    
    topic = headline.find_element(By.TAG_NAME , 'h2').text
    description = headline.find_element(By.TAG_NAME , 'p').text
    link  = headline.find_element(By.TAG_NAME , 'a').get_attribute('href')

    topics.append(topic)
    descriptions.append(description)
    links.append(link)

time.sleep(1)
driver.quit()

df = pd.DataFrame({
    'Topic' : topics,
    'Description' : descriptions,
    'Link' : links
}, index=[i+1 for i in range(len(topics))])


app_path = os.path.dirname(sys.executable)

date_month_year = datetime.now().strftime("%#d-%m-%Y %a")
file_name = f"{date_month_year}.csv"

final_path = os.path.join(app_path, file_name)

df.to_csv(final_path)