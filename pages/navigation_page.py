from playwright.sync_api import Page, Playwright, expect, Locator
from pages.base_page import BasePage


class NavigationPage(BasePage):
    def __init__(self, page: Page, playwright: Playwright):
        super().__init__(page, playwright)

        self.hamburger_menu = page.get_by_role("button", name="Open Menu")
        self.menu_wrapper = page.locator("[class='bm-menu-wrap']")
        self.menu_all_items_button = page.get_by_role(role="link", name="All Items")
        self.menu_about_button = page.get_by_role(role="link", name="About")
        self.menu_logout_button = page.get_by_role(role="link", name="Logout")
        self.menu_reset_app_button = page.get_by_role(role="link", name="Reset App State")
        self.close_menu_button = page.get_by_role(role="button", name="Close Menu")
        self.link_button_x = page.locator("[class='social_twitter']")
        self.link_button_fb = page.locator("[class='social_facebook']")
        self.link_button_li = page.locator("[class='social_linkedin']")

    def open_side_menu(self):
        self.hamburger_menu.click()
        expect(self.menu_wrapper).to_be_visible()

    def close_side_menu(self):
        self.close_menu_button.click()
        expect(self.menu_wrapper).not_to_be_visible()

    def click_link_and_expect_new_tab_to_have_url(self, locator: Locator, expected_url: str):
        with self.page.context.expect_page() as new_page:
            locator.click()

        new_tab = new_page.value
        new_tab.wait_for_load_state()
        assert new_tab.url == expected_url
