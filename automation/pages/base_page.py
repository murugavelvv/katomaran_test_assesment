import pytest
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def wait_for_url(self, url_part: str, timeout: int = 10000):
        """Wait for the URL to contain a specific string."""
        self.page.wait_for_url(f"**/{url_part}**", timeout=timeout)

    def click_element(self, selector: str):
        """Click an element after waiting for it to be visible."""
        self.page.locator(selector).wait_for(state="visible")
        self.page.locator(selector).click()

    def fill_input(self, selector: str, text: str):
        """Fill an input field after waiting for it to be visible."""
        self.page.locator(selector).wait_for(state="visible")
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        """Get the text content of an element."""
        self.page.locator(selector).wait_for(state="visible")
        return self.page.locator(selector).text_content()

    def is_visible(self, selector: str) -> bool:
        """Check if an element is visible."""
        return self.page.locator(selector).is_visible()
