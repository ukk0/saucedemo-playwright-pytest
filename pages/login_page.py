from playwright.sync_api import Page, Playwright, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page, playwright: Playwright):
        super().__init__(page, playwright)

        self.user_name_input = page.get_by_test_id("username")
        self.user_password_input = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-button")
        self.login_error_message = page.get_by_test_id("error")

    def enter_credentials_and_try_login(
        self, username: str = None, password: str = None
    ):
        if username:
            self.user_name_input.fill(username)
        if password:
            self.user_password_input.fill(password)
        self.login_button.click()

    def expect_login_error_with_text(self, text: str):
        expect(self.login_error_message).to_be_visible()
        expect(self.login_error_message).to_have_text(text)
