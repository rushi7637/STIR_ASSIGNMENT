from selenium import webdriver
from selenium.webdriver.chrome.service import Service # type: ignore
from pymongo import MongoClient
import datetime

# Set up MongoDB connection
client = MongoClient('localhost', 27017)
db = client['twitter_trends']
collection = db['trends']

# Set up Selenium with the correct Service class
service = Service("path/to/chromedriver")  # Update this to the actual path to your ChromeDriver executable
driver = webdriver.Chrome(service=service)

driver.get("https://twitter.com/login")

# Log in to Twitter (add your credentials)
username = driver.find_element("name", "session[username_or_email]")
password = driver.find_element("name", "session[password]")
username.send_keys("@patil_p18898")
password.send_keys("Rushi@123")
password.submit()

# Fetch trending topics
trending_topics = driver.find_elements("xpath", "//section[contains(@aria-labelledby, 'accessible-list')]/div/div/span")
trends = [topic.text for topic in trending_topics[:5]]

# Record the data
record = {
    "unique_id": str(datetime.datetime.now().timestamp()),
    "trend1": trends[0],
    "trend2": trends[1],
    "trend3": trends[2],
    "trend4": trends[3],
    "trend5": trends[4],
    "date_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "ip_address": "Proxy IP if applicable"
}
collection.insert_one(record)

driver.quit()
