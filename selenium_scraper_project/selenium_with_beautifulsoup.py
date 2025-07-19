from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import csv
import time

# Setup Selenium WebDriver
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Load the web page
driver.get("https://realpython.github.io/fake-jobs/")
time.sleep(2)  # wait for JavaScript content to load

# Get the fully rendered HTML
html = driver.page_source

# Parse with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all job cards
job_cards = soup.find_all("div", class_="card-content")

# Open CSV for writing
with open("jobs_2.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location"])

    for card in job_cards:
        title = card.find("h2", class_="title").text.strip()
        company = card.find("h3", class_="company").text.strip()
        location = card.find("p", class_="location").text.strip()
        
        print(f"{title} | {company} | {location}")
        writer.writerow([title, company, location])

# Quit browser
driver.quit()
