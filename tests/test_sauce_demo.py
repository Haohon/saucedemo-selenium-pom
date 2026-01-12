import pytest
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

# Load the variables from the .env file
load_dotenv()

# Get the credentials
USER = os.getenv("SAUCE_USERNAME")
PWD = os.getenv("SAUCE_PASSWORD")
URL = os.getenv("BASE_URL")

def test_valid_login_and_add_to_cart(driver):
    driver.get(URL) # Use variable instead of hardcoded link
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.login(USER, PWD) # Use fetched credentials
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_count() == "1"

def test_full_checkout_flow(driver):
    driver.get(URL)
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.login(USER, PWD)
    inventory_page.add_backpack_to_cart()
    checkout_page.complete_checkout("Haohon", "Tester", "12345")
    assert checkout_page.get_confirmation_message() == "Thank you for your order!"