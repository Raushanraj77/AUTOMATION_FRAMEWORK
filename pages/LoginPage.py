from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    TXT_USERNAME = (By.NAME, "username")
    TXT_PASSWORD = (By.NAME, "password")
    BTN_LOGIN = (By.XPATH, "//button[@type='submit']")
    MSG_INVALIDCREDS = (By.XPATH,"//*[@id='app']//div[1]/p")
    MSG_EMPTYCREDS = (By.XPATH, "//*[@id='app']//div//span")

    """Constructor of CarrersPage class"""

    def __init__(self, driver):
        super().__init__(driver)

    # def enter_login_credentials(self, user, pwd):
    #     self.input_element(self.TXT_USERNAME, user)
    #     self.input_element(self.TXT_PASSWORD, pwd)        

    def enter_username(self,user):
        self.input_element(self.TXT_USERNAME, user)

    def enter_password(self, pwd):
        self.input_element(self.TXT_PASSWORD, pwd)


    def enter_login(self):
        self.click_element(self.BTN_LOGIN)

    def validateTitle(self):
        assert self.get_title() == "OrangeHRM"

    def validateInvalidCreds(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS) == "Invalid credentials"

    def validateEmptyUsername(self):
        assert self.get_element_text(self.MSG_EMPTYCREDS) == "Required"

    def validateEmptyPassword(self):
        assert self.get_element_text(self.MSG_EMPTYCREDS) == "Requireds"