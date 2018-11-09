from . import base
import lib.locators.results as locators


class ResultsPage(base.BasePage):
    PATH = ''

    def __init__(self, browser):
        super(ResultsPage, self).__init__(browser)
        self.locators = locators.ResultsLocators()

    @property
    def first_search_result(self):
        return self.browser.find_by_css(self.locators.FIRST_RESULT_TITLE)