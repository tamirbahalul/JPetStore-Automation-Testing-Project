from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class jepStoreLoginPage:
    def __init__(self,driver,webDriverWait):
        self.driver=driver
        self.wdw=webDriverWait
        #לפי אלה (שלמטה) - הפונקציות והאוטומציה יודעת למצוא לעשות השמה לשדות הרלוונטיים באתר
        self.signin_link = (By.LINK_TEXT, "Sign In")
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.signon_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.err_message = (By.CSS_SELECTOR, "div.alert.alert-danger.mt-3")

    def navTo(self):
        self.driver.get("https://jpetstore.aspectran.com/")

    def goToLogin(self):
        signin = self.wdw.until(EC.element_to_be_clickable(self.signin_link))
        signin.click()

    def enterUsername(self, username):
        field = self.wdw.until(EC.visibility_of_element_located(self.username_field))
        field.clear()
        field.send_keys(username)

    def enterPassword(self, password):
        field = self.wdw.until(EC.visibility_of_element_located(self.password_field))
        field.clear()
        field.send_keys(password)

    def clickLogin(self):
        button = self.wdw.until(EC.element_to_be_clickable(self.signon_button))
        button.click()

    def get_error_message(self):
        errorMessage = self.wdw.until(EC.visibility_of_element_located(self.err_message))
        return errorMessage.text
