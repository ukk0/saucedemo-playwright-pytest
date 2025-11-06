import pytest


@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "secret_sauce"),
        ("locked_out_user", "secret_sauce"),
        ("not_registered_user", "secret_sauce"),
        ("standard_user", "s3cr3ts4uc3"),
        ("standard_user", ""),
        ("", "secret_sauce"),
    ],
)
def test_valid_and_invalid_login_credentials(
    login_page, pages, username: str, password: str
):
    login_page.navigate_to_page(url=pages["LOGIN_PAGE"])
    login_page.enter_credentials_and_try_login(username=username, password=password)

    if username == "locked_out_user":
        login_page.expect_login_error_with_text(
            text="Epic sadface: Sorry, this user has been locked out."
        )

    elif username == "not_registered_user":
        login_page.expect_login_error_with_text(
            text="Epic sadface: Username and password do not match any user in this service"
        )

    elif password == "s3cr3ts4uc3":
        login_page.expect_login_error_with_text(
            text="Epic sadface: Username and password do not match any user in this service"
        )

    elif not password:
        login_page.expect_login_error_with_text(
            text="Epic sadface: Password is required"
        )

    elif not username:
        login_page.expect_login_error_with_text(
            text="Epic sadface: Username is required"
        )

    else:
        login_page.current_page_should_be(
            expected_url=pages["INVENTORY_PAGE"], title="Products"
        )


def test_login_required_to_access_app(login_page, pages):
    login_page.navigate_to_page(url=pages["INVENTORY_PAGE"])

    login_page.expect_login_error_with_text(
        text="Epic sadface: You can only access '/inventory.html' when you are logged in."
    )
