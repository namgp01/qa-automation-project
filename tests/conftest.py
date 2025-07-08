import pytest
import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        service_obj = Service(r"C:\Users\gpnam\Downloads\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "edge":
        service_obj = Service(r"C:\Users\gpnam\Downloads\driver\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    # 브라우저 선택

    driver.get("https://www.naver.com/")
    # 네이버 메인
    driver.implicitly_wait(2)
    driver.maximize_window()

    with open(r"C:\Users\gpnam\Downloads\RefundCookieData\cookies.json", "r") as f:
        cookies = json.load(f)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()
    time.sleep(2)
    # 쿠키로 로그인

    request.cls.driver = driver

    yield

    driver.quit()