import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

@pytest.fixture(scope="function")
def page():
    """Setup Playwright browser and return page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # set to False to watch tests run
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
