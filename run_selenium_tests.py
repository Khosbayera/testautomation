from selenium import webdriver
from selenium.webdriver.common.by import By
import traceback

driver = webdriver.Chrome()

try:
    driver.get("https://example.com")
    
    # ❌ Intentionally fail the test by asserting something incorrect
    assert "ThisWillNotBeInTheTitle" in driver.title

except Exception as e:
    driver.save_screenshot("failure.png")
    print("❌ Test failed. Screenshot saved.")
    traceback.print_exc()
    exit(1)

finally:
    driver.quit()

