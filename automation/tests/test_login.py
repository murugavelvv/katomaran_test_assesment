import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# Shared Test Data
VALID_EMAIL = "vmurugavel98@gmail.com"
VALID_PASSWORD = "Mugygfoygipuv98"

# Generate 45 invalid email formats
INVALID_EMAILS = [
    "plainaddress", "#@%^%#$@#$@#.com", "@example.com", "Joe Smith <email@example.com>",
    "email.example.com", "email@example@example.com", ".email@example.com", "email.@example.com",
    "email..email@example.com", "email@example.com (Joe Smith)", "email@example", "email@-example.com",
    "email@example.web", "email@111.222.333.44444", "email@example..com", "Abc..123@example.com",
    "”(),:;<>[\]@example.com", "just\"not\"right@example.com", "this\ is\"really\"not\allowed@example.com",
    "testuser@", "testuser.com", "testuser@.com", "testuser@domain", "testuser@domain.",
    "testuser@domain.c", "testuser@domain.com.", "testuser @domain.com", "testuser@ domain.com",
    "testuser@domain.com ", " testuser@domain.com", "email@domain..com", "email@domain.com-",
    "email@domain.com_", "email@domain.com+", "email@domain.com=", "email@domain.com!",
    "email@domain.com?", "email@domain.com*", "email@domain.com^", "email@domain.com%",
    "email@domain.com$", "email@domain.com#", "email@domain.com@", "email@domain.com~",
    "email@domain.com`"
]

# Generate 45 invalid password formats (too short, missing rules, etc.)
INVALID_PASSWORDS = [
    "short", "12345", "password", "PASSWORD", "Password", "Password123", "1234567890",
    "          ", "a" * 50, "!@#$%^&*", "NoNumbersHere!", "nocapitals123!", "NOLOWERCASE123!",
    "NoSpecialChar123", "12345678aA", "A!1" + "a"*20, "Pass word 1!", "Pass\tword1!",
    "Pass\nword1!", "Pass\rword1!", "Pass\0word1!", "Pass\bword1!", "Pass\fword1!",
    "Pass\vword1!", "Pass\\word1!", "Pass\'word1!", "Pass\"word1!", "Pass\?word1!",
    "Pass\*word1!", "Pass\+word1!", "Pass\-word1!", "Pass\=word1!", "Pass\_word1!",
    "Pass\|word1!", "Pass\/word1!", "Pass\<word1!", "Pass\>word1!", "Pass\{word1!",
    "Pass\}word1!", "Pass\[word1!", "Pass\]word1!", "Pass\(word1!", "Pass\)word1!",
    "Pass\^word1!", "Pass\%word1!"
]

# 10 SQL Injections
SQL_INJECTIONS = [
    "' OR 1=1 --", "' OR '1'='1", "admin' --", "admin' #", "' OR 1=1/*",
    "') OR ('1'='1", "') OR '1'='1--", "') OR 1=1--", "' UNION SELECT 1, 'anotheruser', 'doesntmatter', 1--",
    "' UNION SELECT 1, 1, 1, 1--"
]

# 10 XSS Payloads
XSS_PAYLOADS = [
    "<script>alert(1)</script>", "<img src=x onerror=alert(1)>", "<svg/onload=alert(1)>",
    "<body onload=alert(1)>", "<iframe src=javascript:alert(1)>", "<math><mi>//<maction actiontype=statusline#",
    "\"><script>alert(1)</script>", "'><script>alert(1)</script>", "<script>alert(document.cookie)</script>",
    "<a href=\"javascript:alert(1)\">Click me</a>"
]

class TestLogin:
    
    def test_successful_login(self, page: Page):
        """TC_001: Verify successful login with valid credentials."""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.full_login(VALID_EMAIL, VALID_PASSWORD)
        login_page.click_ok_if_present()
        search_btn = page.get_by_role("button", name="Search Location")
        expect(search_btn).to_be_visible(timeout=10000)

    @pytest.mark.parametrize("invalid_email", INVALID_EMAILS)
    def test_login_invalid_email_formats(self, page: Page, invalid_email):
        """TC_002: Verify application blocks all invalid email formats."""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.enter_email(invalid_email)
        login_page.click_continue()
        assert login_page.is_password_field_visible() is False, f"Allowed invalid email: {invalid_email}"

    @pytest.mark.parametrize("invalid_password", INVALID_PASSWORDS)
    def test_login_invalid_passwords(self, page: Page, invalid_password):
        """TC_003: Verify application rejects invalid passwords."""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.full_login(VALID_EMAIL, invalid_password)
        login_btn = page.get_by_role("button", name="Login")
        expect(login_btn).to_be_visible()

    @pytest.mark.parametrize("payload", SQL_INJECTIONS)
    def test_sql_injection_email(self, page: Page, payload):
        """TC_004: Security - Test SQL Injections in email."""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.enter_email(payload)
        login_page.click_continue()
        assert login_page.is_password_field_visible() is False

    @pytest.mark.parametrize("payload", XSS_PAYLOADS)
    def test_xss_email(self, page: Page, payload):
        """TC_005: Security - Test XSS Payloads in email."""
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.enter_email(payload)
        login_page.click_continue()
        assert login_page.is_password_field_visible() is False
