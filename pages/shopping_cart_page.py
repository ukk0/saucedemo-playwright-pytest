from playwright.sync_api import Page, Playwright

from pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    def __init__(self, page: Page, playwright: Playwright):
        super().__init__(page, playwright)

        self.remove_item_button = page.get_by_text(text="Remove")
        self.cart_item_label = page.locator(
            "[class='cart_list'] [class='cart_item_label']"
        )
        self.return_to_shop_page_button = page.get_by_test_id("continue-shopping")
        self.proceed_to_checkout_button = page.get_by_test_id("checkout")

    def remove_first_item_from_cart(self):
        self.remove_item_button.first.click()

    def get_cart_item_count(self):
        return self.cart_item_label.count()

    def return_to_shop_page(self):
        self.return_to_shop_page_button.click()

    def proceed_to_checkout_page(self):
        self.proceed_to_checkout_button.click()
