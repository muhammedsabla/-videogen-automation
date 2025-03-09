from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

driver_path = "/path/to/chromedriver"  # Update the path to ChromeDriver

chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in full screen
chrome_options.add_argument("--headless")  # Run browser in headless mode (optional)
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "/path/to/download/folder",  # Set download folder
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://videogen.ai")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    create_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Create Video')]"))
    )
    create_button.click()

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Download')]"))
    )

    download_button = driver.find_element(By.XPATH, "//button[contains(text(),'Download')]")
    download_button.click()

    time.sleep(5)
    print("Video downloaded successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
