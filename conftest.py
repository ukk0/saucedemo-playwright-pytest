import pytest

from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.shopping_cart_page import ShoppingCartPage


def login_cookie():
    """
    Allows to bypass the login page for non-login related tests.
    """
    return {
        "name": "session-username",
        "value": "standard_user",
        "domain": "www.saucedemo.com",
        "path": "/",
    }


def fill_cart_script():
    """
    Prefills shopping cart with items.
    """
    return "localStorage.setItem('cart-contents', '[0, 1, 2, 3, 4, 5]')"


@pytest.fixture
def pages():
    return {
        "ABOUT_PAGE": "https://saucelabs.com/",
        "LOGIN_PAGE": "https://www.saucedemo.com/",
        "INVENTORY_PAGE": "https://www.saucedemo.com/inventory.html",
        "CART_PAGE": "https://www.saucedemo.com/cart.html",
        "CHECKOUT_PAGE1": "https://www.saucedemo.com/checkout-step-one.html",
        "CHECKOUT_PAGE2": "https://www.saucedemo.com/checkout-step-two.html",
        "CHECKOUT_PAGE3": "https://www.saucedemo.com/checkout-complete.html",
        "SOC_X_PAGE": "https://x.com/saucelabs",
        "SOC_FB_PAGE": "https://www.facebook.com/saucelabs",
        "SOC_LI_PAGE": "https://www.linkedin.com/company/sauce-labs/",
    }


@pytest.fixture
def login_page(page, playwright):
    return LoginPage(page, playwright)


@pytest.fixture
def inventory_page(page, playwright):
    page.context.add_cookies([login_cookie()])
    return InventoryPage(page, playwright)


@pytest.fixture
def navigation_page(page, playwright):
    page.context.add_cookies([login_cookie()])
    return NavigationPage(page, playwright)


@pytest.fixture
def cart_page(page, playwright):
    page.context.add_cookies([login_cookie()])
    page.context.add_init_script(fill_cart_script())
    return ShoppingCartPage(page, playwright)


@pytest.fixture
def checkout_page(page, playwright):
    page.context.add_cookies([login_cookie()])
    page.context.add_init_script(fill_cart_script())
    return CheckoutPage(page, playwright)
