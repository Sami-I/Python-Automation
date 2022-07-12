from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import pandas as pd
from datetime import datetime
import os
import sys

# Get access to the path attribute
application_path = os.path.dirname(sys.executable)

# Use datetime to add to the filename
date_now = datetime.now()
# MMDDYYYY strftime.org
month_day_year = date_now.strftime("%m%d%y")

# Define the website and the path we're using
website = "https://www.thesun.co.uk/sport/football/"
path = "/usr/local/bin/chromedriver"

# Initiate instance of options to set headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

# Get all the elements represented by the xpath - title and subtitle
containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

# Lists for each html element/text to build our dataframe
titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by='xpath', value='./a/h2').text
    titles.append(title)
    subtitle = container.find_element(by='xpath', value='./a/p').text
    subtitles.append(subtitle)
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    links.append(link)

# Create our dataframe
headlines_dict = {'titles': titles, 'subtitles': subtitles, 'links': links}
df_headlines = pd.DataFrame(headlines_dict)

# Create file to export headlines to a csv file
file_name = f'headlines-{month_day_year}.csv'
final_path = os.path.join(application_path,file_name)
df_headlines.to_csv(final_path)

# Quit driver after extracting information
driver.quit()