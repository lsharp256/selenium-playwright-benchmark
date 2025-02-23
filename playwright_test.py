from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        start = time.perf_counter()
        page.goto("https://en.wikipedia.org/wiki/Main_Page")
        
        search = page.wait_for_selector("#searchInput")
        search.fill("Artificial intelligence")
        
        page.click("#mp-tfa a:has-text('Featured article')")
        
        page.wait_for_selector("#firstHeading")
        
        execution_time = time.perf_counter() - start
        print(f"PLAYWRIGHT_RESULT:{execution_time}")
        
        page.close()
        browser.close()

if __name__ == "__main__":
    run()