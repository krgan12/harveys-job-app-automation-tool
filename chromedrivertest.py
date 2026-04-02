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
    email_input = wait.until(EC.presence_of_all_elements_located((By.ID, "request_anonymous_requester_email")))
    email_input.send_keys(data["email"])

    # Name
    name_input = driver.find_element(By.ID, "request_custom_fields_114100716231")
    name_input.send_keys(data["name"])    

    # Phone
    phone_input = driver.find_element(By.ID, "request_custom_fields_114100726471")
    phone_input.send_keys(data["phone"])

def select_location(driver, location):
    province_dropdown = Select(driver.find_element(By.ID, "province_field_id"))
    province_dropdown.select_by_visible_text(location["province"])

    time.sleep(1)

    city_dropdown = Select(driver.find_element(By.ID, "city_field_id"))
    city_dropdown.select_by_visible_text(location["city"])

    time.sleep(1)

    store_dropdown = Select(driver.find_element(By.ID, "store_field_id"))
    store_dropdown.select_by_visible_text(location["store"])

    checkboxes = driver.find_elements(By.NAME, "roles")
    for cb in checkboxes:
        if cb.get_attributes("value") in user_data["roles"]:
            cb.click()
    

    
    upload = driver.find_element(By.XPATH, "//input[@type='file']")
    upload.send_keys(user_data["resume_path"])   

for location in locations:
    driver.get(URL)

    fill_form(driver, user_data, location) 
    select_location(driver, location)

    # Submit
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

    time.sleep(5) # wait for submission

input("Press Enter to close the browser...")