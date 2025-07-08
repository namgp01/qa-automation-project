from selenium.webdriver.common.by import By

class SeriesPage:

    def __init__(self, driver):
        self.driver = driver

    cash_btn = (By.XPATH, "//a[@class='cash_charge']")
    expect_menu = (By.XPATH, "//h2[@class='area_title_info']")
    cookie_100 = (By.XPATH, "//a[@class='shop_cookie_price _openCookiePurchasePopup(PASS_G_1_40,1,100.0) N=a:cok.buyck']")
    pay_btn = (By.XPATH, "//button[contains(text(),'원 결제하기')]")
    info_btn = (By.XPATH, "//a[@class='N=a:cok.purchase']")
    refund_btn = (By.XPATH, "//a[contains(text(),'구매취소')]")
    accept_btn = (By.XPATH, "//button[@class='area_button_cancel_purchase btn_accp dialog-confirm']")
    done_btn = (By.XPATH, "//a[@href='#'][contains(text(),'확인')]")
    expect_txt = (By.XPATH, "//strong[@class='pop_notice']")

    def click_cash(self):
        return self.driver.find_element(*SeriesPage.cash_btn).click()

    def find_menu(self):
        return self.driver.find_element(*SeriesPage.expect_menu).text

    def click_100(self):
        return self.driver.find_element(*SeriesPage.cookie_100).click()

    def click_pay(self):
        return self.driver.find_element(*SeriesPage.pay_btn).click()

    def click_info(self):
        return self.driver.find_element(*SeriesPage.info_btn).click()

    def get_refund(self):
        return self.driver.find_elements(*SeriesPage.refund_btn)

    def click_accept(self):
        return self.driver.find_element(*SeriesPage.accept_btn).click()

    def click_done(self):
        return self.driver.find_element(*SeriesPage.done_btn).click()

    def find_txt(self):
        return self.driver.find_element(*SeriesPage.expect_txt).text