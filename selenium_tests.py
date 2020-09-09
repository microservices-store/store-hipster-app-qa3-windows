import time

from selenium import webdriver
from datetime import datetime
from junit_xml import TestSuite, TestCase

# datetime object containing current date and time
now = datetime.now()
 
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Initialize the driver
driver = webdriver.Chrome()
# Open provided link in a browser window using the driver
driver.get("http://34.67.97.28/")


test_cases = [TestCase('Test1', 'home.page', 123.345, driver.title , '')]
ts = TestSuite("Selenium Test Suite", test_cases)
# pretty printing is on by default but can be disabled using prettyprint=False
print(TestSuite.to_xml_string([ts]))

driver.quit()
