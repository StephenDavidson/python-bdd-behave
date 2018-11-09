from . import base


class HomeLocators(base.BaseLocators):

    SEARCH_FIELD = 'search_form_input_homepage'
    SEARCH_BUTTON = 'search_button_homepage'

    def __init__(self):
        super(HomeLocators, self).__init__()