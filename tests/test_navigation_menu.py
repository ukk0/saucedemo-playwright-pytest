import pytest


def test_check_side_menu_contents_and_functionality(navigation_page, pages):
    navigation_page.navigate_to_page(url=pages["INVENTORY_PAGE"], title="Products")
    navigation_page.open_side_menu()

    assert navigation_page.menu_all_items_button.is_visible()
    assert navigation_page.menu_about_button.is_visible()
    assert navigation_page.menu_logout_button.is_visible()
    assert navigation_page.menu_reset_app_button.is_visible()
    navigation_page.close_side_menu()


@pytest.mark.parametrize("menu_option", ["All Items", "About", "Logout"])
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


@pytest.mark.parametrize("social_media", ["X", "Facebook", "LinkedIn"])
def test_footer_social_media_navigation(navigation_page, pages, social_media):
    navigation_page.navigate_to_page(url=pages["INVENTORY_PAGE"], title="Products")

    if social_media == "X":
        navigation_page.click_link_and_expect_new_tab_to_have_url(
            locator=navigation_page.link_button_x, expected_url=pages["SOC_X_PAGE"]
        )
    elif social_media == "Facebook":
        navigation_page.click_link_and_expect_new_tab_to_have_url(
            locator=navigation_page.link_button_fb, expected_url=pages["SOC_FB_PAGE"]
        )
    elif social_media == "LinkedIn":
        navigation_page.click_link_and_expect_new_tab_to_have_url(
            locator=navigation_page.link_button_li, expected_url=pages["SOC_LI_PAGE"]
        )
