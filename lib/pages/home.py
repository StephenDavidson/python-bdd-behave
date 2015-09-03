import base
import lib.locators.home as locators


class HomePage(base.BasePage):
    PATH = ''

    def __init__(self, browser):
        super(HomePage, self).__init__(browser)
        self.locators = locators.HomeLocators()

    @property
    def search_field(self):
        return self.browser.find_by_id(self.locators.SEARCH_FIELD)[0]

    @property
    def search_button(self):
        return self.browser.find_by_id(self.locators.SEARCH_BUTTON)[0]

    @property
    def first_search_result(self):
        return self.browser.find_by_css(self.locators.FIRST_RESULT_TITLE)