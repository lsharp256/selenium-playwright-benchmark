import subprocess
import sys
import timeit
import statistics  # For statistical analysis

def run_benchmark(iterations):  # Added iterations parameter
    python_executable = sys.executable

    selenium_times = []
    playwright_times = []

    for i in range(iterations):
        print(f"Iteration {i+1}/{iterations}:")

        # Selenium Test
        print("Running Selenium test...")
        selenium_output = subprocess.run(
            [python_executable, "selenium_test.py"],
            capture_output=True,
            text=True
        )

        if "SELENIUM_RESULT" in selenium_output.stdout:
            try:
                selenium_time_str = selenium_output.stdout.split("SELENIUM_RESULT:")[-1].strip()
                selenium_time = float(selenium_time_str)
                selenium_times.append(selenium_time)  # Store the time
            except ValueError:
                print("Error: Invalid Selenium time format:", selenium_output.stdout)
                return
        else:
            print("Selenium test failed. Error:", selenium_output.stdout)
            return

        # Playwright Test
        print("Running Playwright test...")
        playwright_output = subprocess.run(
            [python_executable, "playwright_test.py"],
            capture_output=True,
            text=True
        )

        if "PLAYWRIGHT_RESULT" in playwright_output.stdout:
            try:
                playwright_time_str = playwright_output.stdout.split("PLAYWRIGHT_RESULT:")[-1].strip()
                playwright_time = float(playwright_time_str)
                playwright_times.append(playwright_time)  # Store the time
            except ValueError:
                print("Error: Invalid Playwright time format:", playwright_output.stdout)
                return
        else:
            print("Playwright test failed. Error:", playwright_output.stdout)
            return

    # Statistical Analysis
    print("\nResults:")
    print("Selenium:")
    print(f"  Average: {statistics.mean(selenium_times):.2f}s")
    print(f"  Median: {statistics.median(selenium_times):.2f}s")
    print(f"  Standard Deviation: {statistics.stdev(selenium_times) if len(selenium_times) > 1 else 0:.2f}s")  # Handle single-run case

    print("Playwright:")
    print(f"  Average: {statistics.mean(playwright_times):.2f}s")
    print(f"  Median: {statistics.median(playwright_times):.2f}s")
    print(f"  Standard Deviation: {statistics.stdev(playwright_times) if len(playwright_times) > 1 else 0:.2f}s")

    # Comparison (using average times)
    average_difference = statistics.mean(selenium_times) - statistics.mean(playwright_times)
    print(f"Average Difference: {average_difference:.2f}s")


if __name__ == "__main__":
    iterations = 10  # Default number of iterations
    if len(sys.argv) > 1:
        try:
            iterations = int(sys.argv[1])
        except ValueError:
            print("Invalid number of iterations. Using default.")

    run_benchmark(iterations=10)