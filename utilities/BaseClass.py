import pytest
import inspect
import logging

from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:

    def select_options(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_log(self):
        logname = inspect.stack()[1][3]
        log = logging.getLogger(logname)

        if not log.handlers:
            file_handler = logging.FileHandler(r"C:\Users\gpnam\PycharmProjects\CookieTesting\reports\logfile.log", encoding="utf-8")
            formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
            file_handler.setFormatter(formatter)
            log.addHandler(file_handler)
            log.setLevel(logging.INFO)

        return log