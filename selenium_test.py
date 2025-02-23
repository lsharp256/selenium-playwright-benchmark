from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

def run():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")  # Set window size
    
    start = time.perf_counter()
    try:
        driver = webdriver.Chrome(options=options)
        
        # Open Wikipedia
        driver.get("https://en.wikipedia.org/wiki/Main_Page")
        
        # Print the page source for debugging
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        
        # Take a screenshot for debugging
        driver.save_screenshot("debug.png")
        
        # Wait for the search input to be visible and interactable
        search = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "searchInput"))
        )
        search.send_keys("Artificial intelligence")
        
        # Wait for the featured article link to be clickable
        featured_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mp-tfa a"))
        )
        featured_link.click()
        
        # Wait for the new page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "firstHeading")))
        
        execution_time = time.perf_counter() - start
        print(f"SELENIUM_RESULT:{execution_time}")
    
    except Exception as e:
        print(f"SELENIUM_ERROR:{str(e)}\n{traceback.format_exc()}")
    
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    run()