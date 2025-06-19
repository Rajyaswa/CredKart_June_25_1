from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Login_Page_Class:
    text_username_id = "username"  # If using name= use By.NAME
    text_password_id = "password"
    button_login_class = "orangehrm-login-button"
    click_menu_button_class = "oxd-userdropdown-name"
    click_logout_link_css = "a[href='/web/index.php/auth/logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 4)

    def Enter_Username(self, Username):
        self.wait.until(EC.presence_of_element_located((By.NAME, self.text_username_id)))
        self.driver.find_element(By.NAME, self.text_username_id).send_keys(Username)

    def Enter_Password(self, password):
        self.driver.find_element(By.NAME, self.text_password_id).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(By.CLASS_NAME, self.button_login_class).click()

    def Click_Menu_Button(self):
        self.driver.find_element(By.CLASS_NAME, self.click_menu_button_class).click()

    def Click_Logout_Link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.click_logout_link_css).click()

    def verify_menu(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, self.click_menu_button_class)))
            return "Pass"
        except:
            return "Fail"
