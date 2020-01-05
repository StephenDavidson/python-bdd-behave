from . import base


class HomeLocators(base.BaseLocators):

    SEARCH_FIELD = '.search__input--adv'
    SEARCH_BUTTON = '.search__button'

    def __init__(self):
        super(HomeLocators, self).__init__()
