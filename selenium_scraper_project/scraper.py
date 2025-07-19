import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Set up Chrome WebDriver
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the job site
driver.get("https://realpython.github.io/fake-jobs/")
driver.maximize_window()
time.sleep(2)

# Fetch job cards
jobs = driver.find_elements(By.CLASS_NAME, "card-content")

# Prepare CSV file
with open("jobs.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location"])  # CSV Header

    for job in jobs:
        title = job.find_element(By.CLASS_NAME, "title").text
        company = job.find_element(By.CLASS_NAME, "company").text
        location = job.find_element(By.CLASS_NAME, "location").text

        # Print and write to CSV
        print(f"Title: {title}, Company: {company}, Location: {location}")
        writer.writerow([title, company, location])

# Done
driver.quit()
