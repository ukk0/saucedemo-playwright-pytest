import pytest


def test_inventory_item_contents(inventory_page, pages):
    inventory_page.navigate_to_page(url=pages["INVENTORY_PAGE"], title="Products")
    inventory_page.verify_inventory_item_contents()


@pytest.mark.parametrize(
    "filtering_option",
    ["Price (high to low)", "Price (low to high)", "Name (A to Z)", "Name (Z to A)"],
)
def test_item_filtering_options(inventory_page, pages, filtering_option):
    inventory_page.navigate_to_page(url=pages["INVENTORY_PAGE"], title="Products")

    if filtering_option == "Price (high to low)":
        inventory_page.use_inventory_filter(filter_option="hilo")
        inventory_page.verify_items_are_ordered_by_price(reverse=True)

    elif filtering_option == "Price (low to high)":
        inventory_page.use_inventory_filter(filter_option="lohi")
        inventory_page.verify_items_are_ordered_by_price(reverse=False)

    elif filtering_option == "Name (A to Z)":
        inventory_page.use_inventory_filter(filter_option="az")
        inventory_page.verify_items_are_ordered_by_name(reverse=False)

    elif filtering_option == "Name (Z to A)":
        inventory_page.use_inventory_filter(filter_option="za")
        inventory_page.verify_items_are_ordered_by_name(reverse=True)


@pytest.mark.parametrize(
    "to_add, to_remove",
    [
        (1, 1),
        (2, 1),
        (3, 1),
    ],
)
def test_adding_and_removing_cart_items(inventory_page, pages, to_add, to_remove):
    inventory_page.navigate_to_page(url=pages["INVENTORY_PAGE"], title="Products")

    inventory_page.add_items_to_cart(amount_of_items=to_add)
    assert inventory_page.cart_item_count() == to_add

    inventory_page.remove_items_from_cart(amount_of_items=to_remove)
    total_items = to_add - to_remove
    if not total_items:
        inventory_page.verify_cart_has_no_items()
    else:
        assert inventory_page.cart_item_count() == total_items
