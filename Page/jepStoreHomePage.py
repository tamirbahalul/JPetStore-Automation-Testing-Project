import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class jepStoreHomePage:
    def __init__(self,driver,webDriverWait):
        self.driver=driver
        self.wdw=webDriverWait
        self.welcome_text = (By.CSS_SELECTOR, "div.text-end.pb-2")
        self.signout_link = (By.LINK_TEXT, "Sign Out")
        self.menu_button_location_sign_out = (By.ID, "dropdownMenuButton")
        self.signOut_CSS = (By.CSS_SELECTOR, "a[href='/account/signoff']")

    def get_welcome_text(self):
        welcome = self.wdw.until(EC.visibility_of_element_located(self.welcome_text))
        return welcome.text

    #מחכה שהאלמנט יהיה על המסך ולכן חייב לפתוח את התפריט לפני
    def get_sign_out_text(self):
        self.open_dropdown_menu()
        element = self.wdw.until(EC.visibility_of_element_located(self.signout_link))
        return element.text

    def open_dropdown_menu(self):
        element_click = self.wdw.until(
            EC.element_to_be_clickable(self.menu_button_location_sign_out))
        element_click.click()

    #עושה יציאה מהמשתמש ברגע שהקודם היה נכון בשביל לצאת מהסשן
    def is_before_succ_login(self):
        self.open_dropdown_menu()
        time.sleep(0.5)
        # התפריט פתוח אך ב2 השורות למטה השתמשנו בפעולות שלא מחייבות להמתין לתפריט משום שיש עם זה בעיות
        # דרך JS יודע ללחוץ וללכת לארגומנט וגם until located כאן לא חייב שיראו בפתיחת תפריט
        button = self.wdw.until(EC.presence_of_element_located(self.signOut_CSS))
        self.driver.execute_script("arguments[0].click();", button)

    # שני הפונקציות למטה נועדו לבחון אם אנחנו עומדים בציפייה לעומת התוצאה בפועל
    # מחזיר כן או לא בוליאני בבדיקה אם גדול מ0 זה אומר שקיים אלמנט יציאה ואנחנו בפנים וככה אפשר לדעת אם הציפייה הצליחה בפועל
    # חייב כוכבית כי find מקבל 2 ערכים והכובית יודעת לפריד את הערך מהמפתח כדי שיעבוד וימצא
    def is_logged_in(self):
        element_is_exist = self.driver.find_elements(*self.signOut_CSS)
        return len(element_is_exist) > 0


