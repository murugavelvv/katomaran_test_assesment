from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.url = "https://tichi-app-webapp-stage.web.app/login"
        
    def navigate(self):
        self.page.goto(self.url)
        
    def enter_email(self, email: str):
        email_input = self.page.get_by_role("textbox", name="Email Address *")
        email_input.wait_for(state="visible")
        email_input.fill(email)
        
    def click_continue(self):
        continue_btn = self.page.get_by_role("button", name="Continue", exact=True)
        continue_btn.click()
             
    def enter_password(self, password: str):
        password_input = self.page.get_by_role("textbox", name="Password *")
        password_input.wait_for(state="visible", timeout=5000)
        password_input.fill(password)
        
    def click_login(self):
        login_btn = self.page.get_by_role("button", name="Login")
        login_btn.click(force=True)

    def full_login(self, email: str, password: str):
        self.enter_email(email)
        self.click_continue()
        self.enter_password(password)
        self.click_login()
        
    def is_password_field_visible(self) -> bool:
        try:
            self.page.get_by_role("textbox", name="Password *").wait_for(state="visible", timeout=500)
            return True
        except:
            return False
            
    def click_ok_if_present(self):
        try:
            self.page.get_by_role("button", name="Ok").wait_for(state="visible", timeout=5000)
            self.page.get_by_role("button", name="Ok").click()
        except:
            pass
