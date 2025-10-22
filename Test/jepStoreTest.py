from Page.jepStoreHomePage import jepStoreHomePage
from Page.jepStoreLoginPage import jepStoreLoginPage
import time

class JPetStoreTest:
    def __init__(self, driver, webDriverWait):
        self.driver = driver
        self.wdw = webDriverWait
    #פונקציית הבדיקה
    def script(self, username, password, expected, beforeLogin):
        pageLogin = jepStoreLoginPage(self.driver, self.wdw)
        pageHome = jepStoreHomePage(self.driver, self.wdw)
        if beforeLogin == True:
            pageHome.is_before_succ_login()
            pageLogin.goToLogin()
            pageLogin.enterUsername(username)
            pageLogin.enterPassword(password)
            pageLogin.clickLogin()
        else:
            pageLogin.navTo()
            pageLogin.goToLogin()
            pageLogin.enterUsername(username)
            pageLogin.enterPassword(password)
            pageLogin.clickLogin()

        resultIsGood = pageHome.is_logged_in()
        # בדיקה של תוצאה צפויה
        """בודק אם ההתחברות הצליחה"""
        if expected == "success":
            if resultIsGood:
                print(f" PASS - התחברות הצליחה כמו שציפינו ({username}/{password})")
                welcome_message = pageHome.get_welcome_text()
                sign_out_message = pageHome.get_sign_out_text()
                print(f"{welcome_message}")
                print(f"{sign_out_message}")
            else:
                print(f"ERROR - ציפינו להתחברות אבל נכשל ({username}/{password})")
                error_msg = pageLogin.get_error_message()
                print(f"{error_msg}")
        else:
            if resultIsGood:
                print(f"ERROR - ציפינו לכישלון אבל הצליחה ({username}/{password})")
            else:
                print(f" FAIL - ההתחברות נכשלה כמו שציפינו ({username}/{password})")


