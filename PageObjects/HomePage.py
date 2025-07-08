from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    menu_btn = (By.XPATH, "//span[@class='service_icon type_more']")
    series_btn = (By.XPATH, "//a[@href='https://series.naver.com/']")
    event_pop = (By.XPATH, "//button[@class='close_btn']")
    login_btn = (By.XPATH, "//li/a/span[@class='gnb_txt']")
    input_id = (By.XPATH, "//input[@id='id']")
    input_pw = (By.XPATH, "//input[@id='pw']")
    login_btn2 = (By.XPATH, "//button[@id='log.login']")

    def click_menu(self):
        return self.driver.find_element(*HomePage.menu_btn).click()

    def click_series(self):
        return self.driver.find_element(*HomePage.series_btn).click()

    def close_event(self):
        return self.driver.find_element(*HomePage.event_pop)

    def click_login(self):
        return self.driver.find_element(*HomePage.login_btn).click()

    def get_id(self):
        return self.driver.find_element(*HomePage.input_id)

    def get_pw(self):
        return self.driver.find_element(*HomePage.input_pw)

    def click_login2(self):
        return self.driver.find_element(*HomePage.login_btn2).click()