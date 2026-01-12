import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_valid_login_and_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()
    
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    assert inventory_page.get_cart_count() == "1"

@pytest.mark.parametrize("username, password, expected_error", [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("wrong_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service")
])
def test_invalid_login_scenarios(driver, username, password, expected_error):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert expected_error in login_page.get_error_message()

def test_full_checkout_flow(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()
    checkout_page.complete_checkout("Haohon", "Tester", "12345")
    
    assert checkout_page.get_confirmation_message() == "Thank you for your order!"