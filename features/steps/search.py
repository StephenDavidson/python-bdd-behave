from behave import *

use_step_matcher("re")
"""
Search specific steps
"""


@when("I search for (?P<text>.+)")
def search_for(context, text):
    context.execute_steps('''
        When I enter test into the search field
        And I click on the search button
    ''')
