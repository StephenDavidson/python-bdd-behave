__author__ = 'Stephen'

from home import HomePage
from results import ResultsPage

class PageFactory(object):
    def __new__(cls, page_name):
        try:
            return eval(page_name.title() + 'Page')
        except NameError:
            print 'Unable to find' + page_name.title() + '. Try adding the class to the pages __init__, verify the' \
                                                         'class exists within the pages module, and double check the ' \
                                                         'class spelling'
