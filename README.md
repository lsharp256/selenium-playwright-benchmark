# Selenium vs. Playwright Benchmark
This project compares the execution speed of Selenium and Playwright by running a basic test on Wikipedia. The test involves navigating to the Wikipedia main page, interacting with the search input, and clicking a featured article link.

# Prerequisites
- Python 3.7 or higher
- Chrome or Chromium browser

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/selenium-playwright-benchmark.git
   cd selenium-playwright-benchmark

2. Create and activate a virtual environment: 
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    playwright install

## Running the Benchmark
```python .\benchmark.py```

## Example Output:

You should see something like this:

```Running Selenium test...

DevTools listening on ws://127.0.0.1:57658/devtools/browser/c626968d-e732-4b10-8025-09f938cacc7a
Running Playwright test...

Results:
Selenium Execution Time: 5.86s
Playwright Execution Time: 2.66s
Difference: 3.20s
```