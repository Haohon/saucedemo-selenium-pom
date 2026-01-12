from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_msg = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        self.logger.info(f"Navigating to login with user: {username}")
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.logger.info("Credentials entered, clicking login button.")
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        error = self.driver.find_element(*self.error_msg).text
        self.logger.warning(f"Login failed as expected. Error: {error}")
        return error