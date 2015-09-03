import base


class ResultsLocators(base.BaseLocators):

    FIRST_RESULT_TITLE = '.result__a'

    def __init__(self):
        super(ResultsLocators, self).__init__()