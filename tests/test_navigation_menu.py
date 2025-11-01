import pytest


def test_check_side_menu_contents_and_functionality(navigation_page, pages):
    navigation_page.navigate_to_page(url=pages["INVENTORY_PAGE"], title="Products")
    navigation_page.open_side_menu()

    assert navigation_page.menu_all_items_button.is_visible()
    assert navigation_page.menu_about_button.is_visible()
    assert navigation_page.menu_logout_button.is_visible()
    assert navigation_page.menu_reset_app_button.is_visible()
    navigation_page.close_side_menu()


@pytest.mark.parametrize(
    "menu_option", [
        "All Items",
        "About",
        "Logout"
    ]
)
def test_side_menu_navigation(navigation_page, pages, menu_option):
    navigation_page.navigate_to_page(url=pages["INVENTORY_PAGE"], title="Products")
    navigation_page.open_side_menu()

    if menu_option == "All Items":
        navigation_page.menu_all_items_button.click()
        navigation_page.current_page_should_be(expected_url=pages["INVENTORY_PAGE"])

    elif menu_option == "About":
        navigation_page.menu_about_button.click()
        navigation_page.current_page_should_be(expected_url=pages["ABOUT_PAGE"])

    elif menu_option == "Logout":
        navigation_page.menu_logout_button.click()
        navigation_page.current_page_should_be(expected_url=pages["LOGIN_PAGE"])
