from playwright.sync_api import Page, Playwright, expect


class BasePage:
    def __init__(self, page: Page, playwright: Playwright):
        self.page = page
        self.playwright = playwright
        playwright.selectors.set_test_id_attribute("data-test")
        self.page_subtitle = page.get_by_test_id("title")

    def navigate_to_page(self, url: str, title: str = None):
        self.page.goto(url)
        if title:
            expect(self.page_subtitle).to_have_text(title)

    def current_page_should_be(self, expected_url: str, title: str = None):
        expect(self.page).to_have_url(expected_url)
        if title:
            expect(self.page_subtitle).to_have_text(title)
