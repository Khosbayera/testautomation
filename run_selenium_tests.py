from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback

driver = webdriver.Chrome()

try:
    driver.get("https://example.com")
    assert "Not Expected Title" in driver.title  # Force failure for demo
except Exception:
    driver.save_screenshot("failure.png")
    print("Test failed. Screenshot saved.")
    traceback.print_exc()
    exit(1)
finally:
    driver.quit()
