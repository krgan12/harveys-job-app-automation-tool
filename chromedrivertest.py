from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

URL = "https://harveyscareers.zendesk.com/hc/en-us/requests/new"

user_data = {
    "email": "keagan123@outlook.com",
    "name": "Keagan Rodrigues",
    "phone": "6473355347",
    "roles": ["Cashier", "Garnisher", "Grill/Fryer", "Supervisor", "Manager"],
    "employment_type": ["Full time", "Part time"],
    "availability": {
        "morning": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "afternoon": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "evening": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "late_night": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    },
    "resume_path": "Keagan_Rodrigues_Resume.pdf"
}

locations = [
    {"province": "Ontario", "city": "Mississauga", "store": "-2312- 715 Burnhamthorpe Rd W"} #test location
]

def fill_form(driver, data, location):
    # Email
    
    # Name

    # Phone
    pass

def select_location(driver, location):
    pass

input("Press Enter to close the browser...")