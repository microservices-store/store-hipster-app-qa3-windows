from selenium import webdriver
import time

# Initialize the driver
driver = webdriver.Chrome()
# Open provided link in a browser window using the driver
driver.get("http://34.67.97.28/")
print(driver.title)
driver.quit()
