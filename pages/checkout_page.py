from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def complete_checkout(self, fname, lname, zip_code):
        import time
        wait = WebDriverWait(self.driver, 30)
        
        self.logger.info("Opening shopping cart.")
        cart = wait.until(EC.element_to_be_clickable(self.cart_link))
        self.driver.execute_script("arguments[0].click();", cart)
        
        self.logger.info("Proceeding to Checkout.")
        checkout_btn = wait.until(EC.element_to_be_clickable(self.checkout_button))
        self.driver.execute_script("arguments[0].click();", checkout_btn)
        
        self.logger.info(f"Entering shipping details for: {fname}")
        wait.until(EC.visibility_of_element_located(self.first_name_field)).send_keys(fname)
        self.driver.find_element(*self.last_name_field).send_keys(lname)
        self.driver.find_element(*self.zip_field).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()
        
        # STABILITY: Small sleep to let the final summary page render
        time.sleep(2) 
        
        self.logger.info("Finalizing order.")
        finish = wait.until(EC.presence_of_element_located(self.finish_button))
        self.driver.execute_script("arguments[0].click();", finish)
        
    def get_confirmation_message(self):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(EC.visibility_of_element_located(self.complete_header)).text