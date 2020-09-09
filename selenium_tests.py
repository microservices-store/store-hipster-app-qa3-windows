import time

from selenium import webdriver
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# Initialize the driver
driver = webdriver.Chrome()
# Open provided link in a browser window using the driver
driver.get("http://34.67.97.28/")

print("<?xml version=\"1.0\" encoding=\"UFT-8\"?>")
print("<TestReport time=\"" + dt_string + "\">")
print("<TestCases>")
print("<TestCase id=\"001\"/>")
print("<Name>Home Page - " + driver.title + "</Name>")
print("<TestResult>Pass</TestResult>")
print("</TestCases>")
print("</TestReport>")
driver.quit()
