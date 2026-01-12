from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger() # Fixed AttributeError
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.logger.info("Adding backpack to cart.")
        wait = WebDriverWait(self.driver, 20)
        btn = wait.until(EC.element_to_be_clickable(self.add_backpack))
        # Forced JavaScript click to bypass lag
        self.driver.execute_script("arguments[0].click();", btn)

    def get_cart_count(self):
        self.logger.info("Waiting for cart badge to update...")
        wait = WebDriverWait(self.driver, 25)
        return wait.until(EC.presence_of_element_located(self.cart_badge)).text