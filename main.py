"""
This code was based on some tutorials and searches on forums.
Here are the main sources:

https://www.reddit.com/r/learnpython/comments/19anq1l/using_selenium_for_brave_browser/?rdt=39544
https://youtu.be/NB8OceGZGjA?si=jW95afmNn4wWZvE-
"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Optional: Set up Chrome options, like: specify the binary, activate headless mode etc
# options = Options()

# Create a Service object
service = Service()

# Create driver based on Chrome
driver = webdriver.Chrome(service = service)

# Open the browser with the goal URL beetween "()"
driver.get("https://duckduckgo.com")

# Delay of 4s
time.sleep(4)

# It finds an element (in the example below we select the "Search Bar" by the XPATH name)
input_element = driver.find_element(By.XPATH, '//*[@id="searchbox_input"]')

# The XPATH can be found by: entering the inpection mode, in the HTML submenu right click the element,
# click "Copy" and select "Xpath".


# The keys are written in the selected field and the key "Enter" is automatically pressed
input_element.send_keys("Gold gram quotation today" + Keys.ENTER)

time.sleep(10)

# Close the browser
driver.quit()