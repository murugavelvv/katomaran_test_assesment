import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://tichi-app-webapp-stage.web.app/login")
    page.get_by_role("textbox", name="Email Address *").click()
    page.get_by_role("textbox", name="Email Address *").click()
    page.get_by_role("textbox", name="Email Address *").fill("vmurugavel98@gmail.com")
    page.get_by_role("button", name="Continue", exact=True).click()
    page.get_by_role("textbox", name="Password *").click()
    page.get_by_role("textbox", name="Password *").fill("Mugygfoygipuv98")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Ok").click()
    page.get_by_role("button", name="Search Location").click()
    page.get_by_text("Coimbatore, Tamil Nadu, India").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
