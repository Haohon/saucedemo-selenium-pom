from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.zip_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def complete_checkout(self, fname, lname, zip_code):
        self.driver.find_element(*self.cart_link).click()
        self.driver.find_element(*self.checkout_button).click()
        self.driver.find_element(*self.first_name_field).send_keys(fname)
        self.driver.find_element(*self.last_name_field).send_keys(lname)
        self.driver.find_element(*self.zip_field).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()
        self.driver.find_element(*self.finish_button).click()

    def get_confirmation_message(self):
        return self.driver.find_element(*self.complete_header).text