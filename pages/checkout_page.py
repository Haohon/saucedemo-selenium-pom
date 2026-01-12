from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def complete_checkout(self, fname, lname, zip_code):
        wait = WebDriverWait(self.driver, 15) # Increased to 15 seconds for parallel stability
        
        # 1. Click Cart Link
        cart = wait.until(EC.element_to_be_clickable(self.cart_link))
        cart.click()
        
        # 2. Verify we are on the cart page before looking for the checkout button
        # This helps if the browser is lagging
        wait.until(EC.url_contains("cart.html"))
        
        # 3. Click Checkout
        checkout_btn = wait.until(EC.element_to_be_clickable(self.checkout_button))
        checkout_btn.click()
        
        # 4. Fill Form
        wait.until(EC.visibility_of_element_located(self.first_name_field)).send_keys(fname)
        self.driver.find_element(*self.last_name_field).send_keys(lname)
        self.driver.find_element(*self.zip_field).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()
        
        # 5. Finish
        wait.until(EC.element_to_be_clickable(self.finish_button)).click()

    def get_confirmation_message(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located(self.complete_header)).text