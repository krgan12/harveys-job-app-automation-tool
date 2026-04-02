from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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

input("Press Enter to close the browser...")