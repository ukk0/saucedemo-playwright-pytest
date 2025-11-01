from pages.base_page import BasePage
from playwright.sync_api import Page, Playwright, expect


class CheckoutPage(BasePage):
    def __init__(self, page: Page, playwright: Playwright):
        super().__init__(page, playwright)

        self.submit_info_button = page.get_by_test_id("continue")
        self.input_first_name = page.get_by_placeholder(text="First Name")
        self.input_last_name = page.get_by_placeholder(text="Last Name")
        self.input_zip_code = page.get_by_placeholder(text="Zip/Postal Code")
        self.error_missing_info = page.get_by_test_id("error")
        self.checkout_item_price = page.locator("[class='cart_item'] [class='inventory_item_price']")
        self.summary_subtotal_label = page.get_by_test_id("subtotal-label")
        self.summary_tax_label = page.get_by_test_id("tax-label")
        self.summary_total_label = page.get_by_test_id("total-label")
        self.finish_payment_button = page.get_by_test_id("finish")
        self.thank_you_heading = page.get_by_role(role="heading", name="Thank you for your order!")
        self.return_to_shop_button = page.get_by_test_id("back-to-products")
        self.cancel_checkout_button = page.get_by_test_id("cancel")

    def fill_required_info_and_proceed(
            self, first_name: str = None, last_name: str = None, zip_code: str = None
    ):
        if first_name:
            self.input_first_name.fill(first_name)
        if last_name:
            self.input_last_name.fill(last_name)
        if zip_code:
            self.input_zip_code.fill(zip_code)
        self.submit_info_button.click()

    def expect_missing_info_warning(self, expected_error: str):
        expect(self.error_missing_info).to_have_text(expected_error)

    def cancel_checkout(self):
        self.cancel_checkout_button.click()

    def finalize_payment(self):
        self.finish_payment_button.click()

    def return_to_shop(self):
        self.return_to_shop_button.click()

    def validate_order_price_details(self):
        sum_of_item_prices = sum([
            float(price[1:]) for price in self.checkout_item_price.all_inner_texts()
        ])
        subtotal = float(self.summary_subtotal_label.inner_text().split("$")[1])
        tax = float(self.summary_tax_label.inner_text().split("$")[1])
        total = float(self.summary_total_label.inner_text().split("$")[1])
        assert sum_of_item_prices == subtotal
        assert subtotal + tax == total