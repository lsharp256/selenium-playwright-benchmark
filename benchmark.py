import subprocess
import sys

def run_benchmark():
    # Use the current Python interpreter (from the virtual environment)
    python_executable = sys.executable

    print("Running Selenium test...")
    selenium_output = subprocess.run(
        [python_executable, "selenium_test.py"],  # Use the virtual environment's Python
        capture_output=True,
        text=True
    )
    
    # Check if the Selenium test produced a result
    if "SELENIUM_RESULT" in selenium_output.stdout:
        selenium_time_str = selenium_output.stdout.split("SELENIUM_RESULT:")[-1].strip()
        selenium_time = float(selenium_time_str)
    else:
        print("Selenium test failed. Error:", selenium_output.stdout)
        return  # Exit if Selenium fails
    
    print("Running Playwright test...")
    playwright_output = subprocess.run(
        [python_executable, "playwright_test.py"],  # Use the virtual environment's Python
        capture_output=True,
        text=True
    )
    
    # Check if the Playwright test produced a result
    if "PLAYWRIGHT_RESULT" in playwright_output.stdout:
        playwright_time_str = playwright_output.stdout.split("PLAYWRIGHT_RESULT:")[-1].strip()
        playwright_time = float(playwright_time_str)
    else:
        print("Playwright test failed. Error:", playwright_output.stdout)
        return  # Exit if Playwright fails
    
    # Print results
    print("\nResults:")
    print(f"Selenium Execution Time: {selenium_time:.2f}s")
    print(f"Playwright Execution Time: {playwright_time:.2f}s")
    print(f"Difference: {selenium_time - playwright_time:.2f}s")

if __name__ == "__main__":
    run_benchmark()