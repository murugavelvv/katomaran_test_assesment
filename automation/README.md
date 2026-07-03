# Tichi Playwright Automation Suite

This repository contains the automated tests for the Tichi web application, utilizing **Playwright** with **Python**, **Pytest**, and the **Page Object Model (POM)**.

## Directory Structure

```text
automation/
├── pages/
│   ├── __init__.py
│   ├── base_page.py       # Reusable Playwright wrappers (click, fill, wait)
│   └── login_page.py      # Locators and interactions for Login
├── tests/
│   ├── __init__.py
│   └── test_login.py      # Pytest test cases for login flows
├── conftest.py            # Pytest fixtures for browser setup/teardown
├── pytest.ini             # Optional Pytest configurations
├── requirements.txt       # Dependencies
└── README.md              # Instructions
```

## Setup & Installation

1. Initialize a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install pytest pytest-playwright pytest-html allure-pytest
   ```

3. Install Playwright browsers:
   ```bash
   playwright install chromium
   ```

## Running Tests & Reporting

### 1. Basic Console Run
```bash
pytest tests/
```

### 2. Generate HTML Report (pytest-html)
```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### 3. Generate QA Dashboard Report (Allure)
Allure provides a highly detailed and interactive test report dashboard.

1. Install the Allure command-line tool on your OS:
   - **Windows (Scoop):** `scoop install allure`
   - **Mac (Homebrew):** `brew install allure`

2. Run the tests and output Allure results data:
   ```bash
   pytest tests/ --alluredir=reports/allure-results
   ```

3. Serve the Allure dashboard locally:
   ```bash
   allure serve reports/allure-results
   ```
   This will automatically open an impressive QA dashboard in your default browser.
