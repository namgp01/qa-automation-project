import pytest
import time

from PageObjects.SeriesPage import SeriesPage
from TestData.logindata import LoginData
from utilities.BaseClass import BaseClass
from PageObjects.HomePage import HomePage

class TestRefundCookie(BaseClass):

    expect_title = "네이버 시리즈"
    expect_menu = "나의 이용정보"
    expect_txt = "완료"

    def test_moveto_series(self, get_data):
        log = self.get_log()

        home_page = HomePage(self.driver)

        # home_page.click_login()
        # 로그인 화면 진입

        # home_page.get_id().send_keys(get_data["ID"])
        # home_page.get_pw().send_keys(get_data["PW"])
        # 수동 로그인 정보 입력

        # home_page.click_login2()
        # 수동 로그인 시도

        home_page.click_menu()
        home_page.click_series()
        # 네이버 시리즈 메인 화면 진입

        window_open = self.driver.window_handles
        self.driver.switch_to.window(window_open[1])

        assert self.driver.title == self.expect_title
        log.info(self.driver.title)
        # 타이틀 확인

        home_page.close_event().click()
        # 이벤트 팝업 닫기

    def test_refund_cookie(self):
        log = self.get_log()

        series_page = SeriesPage(self.driver)

        series_page.click_cash()
        # 쿠키 충전 화면 진입

        window_open = self.driver.window_handles
        self.driver.switch_to.window(window_open[2])

        assert series_page.find_menu() == self.expect_menu
        log.info(series_page.find_menu())
        # 메뉴 확인

        # series_page.click_100()
        # 100원 선택

        # self.driver.switch_to.window(window_open[3])
        # 결제 화면 전환

        # series_page.click_pay()
        # 결제 버튼 클릭

        # time.sleep(10)
        # 보안 키패드 수동 입력

        series_page.click_info()
        # 충전 내역 보기

        while True:

            refund_lis = series_page.get_refund()

            if not refund_lis:
                log.info("환불 가능 내역 없음")
                break

            btn = refund_lis[0]
            btn.click()

            series_page.click_accept()
            assert self.expect_txt in series_page.find_txt()
            log.info(series_page.find_txt())
            # 완료 문구 확인
            series_page.click_done()

            time.sleep(1)
        # 구매 취소 반복

        assert not series_page.get_refund()
        # 버튼 미노출 확인

    @pytest.fixture(params=LoginData.get_test_data("1"))
    def get_data(self, request):
        return request.param
        # 엑셀 데이터 받기