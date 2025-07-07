from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ✅ DO NOT point directly to Profile 1 folder
user_dir = r"C:\Users\anton\AppData\Local\Google\Chrome\User Data"
profile_dir = "Profile 1"  # This must match chrome://version/ output

options = Options()
options.add_argument(f"--user-data-dir={user_dir}")
options.add_argument(f"--profile-directory={profile_dir}")
options.add_argument("--start-maximized")

# Optional: these help avoid crashes
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

time.sleep(1)
print("Opening new tab...")
driver.execute_script("window.open('about:blank', '_blank');")
time.sleep(1)

# ✅ Switch to the new tab
print("Switching to new tab...")
driver.switch_to.window(driver.window_handles[-1])

# ✅ Open LinkedIn in the new tab
print("Navigating to LinkedIn...")
driver.get("https://www.linkedin.com")
time.sleep(5)

try:
    searchbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    print("Page loaded successfully")
except:
    print("Error occurred")

# Example: Perform a search (optional)
# searchbox.send_keys("Python Developer")
# searchbox.send_keys(Keys.RETURN)
