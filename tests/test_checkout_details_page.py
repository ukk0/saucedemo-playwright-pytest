import pytest


def test_cancel_checkout_process(checkout_page, pages):
    checkout_page.navigate_to_page(
        url=pages["CHECKOUT_PAGE1"], title="Checkout: Your Information"
    )

    checkout_page.cancel_checkout()
    checkout_page.current_page_should_be(
        expected_url=pages["CART_PAGE"], title="Your Cart"
    )


@pytest.mark.parametrize(
    "fname, lname, zcode",
    [
        ("", "McTester", "123456"),
        ("Testy", "", "123456"),
        ("Testy", "McTester", ""),
        ("Testy", "McTester", "123456"),
    ],
)
def test_buyer_info_is_required_at_checkout(checkout_page, pages, fname, lname, zcode):
    checkout_page.navigate_to_page(
        url=pages["CHECKOUT_PAGE1"], title="Checkout: Your Information"
    )

    checkout_page.fill_required_info_and_proceed(
        first_name=fname, last_name=lname, zip_code=zcode
    )

    if not fname:
        checkout_page.expect_missing_info_warning(
            expected_error="Error: First Name is required"
        )

    elif not lname:
        checkout_page.expect_missing_info_warning(
            expected_error="Error: Last Name is required"
        )

    elif not zcode:
        checkout_page.expect_missing_info_warning(
            expected_error="Error: Postal Code is required"
        )

    else:
        checkout_page.current_page_should_be(
            expected_url=pages["CHECKOUT_PAGE2"], title="Checkout: Overview"
        )
