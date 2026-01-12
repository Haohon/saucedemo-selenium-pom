import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    # This runs before every test
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    # This runs after every test
    driver.quit()

def test_valid_login_and_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Action
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()

    # Assertion
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    assert inventory_page.get_cart_count() == "1"

def test_invalid_login(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    # Action: intentionally wrong password
    login_page.login("standard_user", "wrong_password")

    # Assertion: Verify error message appears
    expected_error = "Epic sadface: Username and password do not match any user in this service"
    assert login_page.get_error_text() == expected_error

    
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") # Runs without a GUI
    options.add_argument("--no-sandbox") # Required for Linux/Docker
    options.add_argument("--disable-dev-shm-usage") # Overcomes resource limits
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(5)
    yield driver
    driver.quit()