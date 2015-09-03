import base


class HomeLocators(base.BaseLocators):

    SEARCH_FIELD = 'search_form_input_homepage'
    SEARCH_BUTTON = 'search_button_homepage'
    FIRST_RESULT_TITLE = 'result__a'

    def __init__(self):
        super(HomeLocators, self).__init__()