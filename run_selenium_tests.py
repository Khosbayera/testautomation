from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback

driver = webdriver.Chrome()

try:
    driver.get("https://example.com")
    assert "ThisWillNotBeInTheTitle" in driver.title
    mongolian student

except Exception as e:
    driver.save_screenshot("failure.png")
    print("❌ Test failed. Screenshot saved.")
    traceback.print_exc()
    exit(1)

finally:
    driver.quit()

