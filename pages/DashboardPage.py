from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class DashboardPage(BasePage):

    TXT_DASHBOARD = (By.XPATH, "//*[@id='app']//header//span/h6")

    def __init__(self, driver):
        super().__init__(driver)

    def validatePageLoaded(self):
        self.verify_element_displayed(self.TXT_DASHBOARD)
        assert self.get_element_text(self.TXT_DASHBOARD) == "Dashboard"