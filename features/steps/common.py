from behave import *
from hamcrest import assert_that, contains_string, equal_to

from lib.pages import PageFactory

use_step_matcher("re")

"""
This file contains steps that are universal to all features.
"""


@step("I visit the (?P<page_name>.+) page")
def visit(context, page_name):
    context.page = PageFactory(page_name)(context.browser)
    context.browser.visit(context.base_url + context.page.PATH)


@then("I should be on the (?P<page_name>.+) page")
def should_be_on_page(context, page_name):
    context.page = PageFactory(page_name)(context.browser)
    assert_that(context.browser.url.lower(), contains_string(context.page.PATH))


@step("I click on the (?P<page_attr>.+)")
def click(context, page_attr):
    page_attr = transform_string_to_page_attr(page_attr)
    getattr(context.page, page_attr).click()


@step("I enter (?P<value>.+) into the (?P<page_attr>.+)")
def enter(context, value, page_attr):
    page_attr = transform_string_to_page_attr(page_attr)
    getattr(context.page, page_attr).fill(value)


@then("the (?P<page_attr>.+) should (?P<negate>|not )be (?P<assertion>visible)")
def should_be(context, page_attr, negate, assertion):
    page_attr = transform_string_to_page_attr(page_attr)
    assert_that(getattr(context.page, page_attr).visible, equal_to(False if negate else True))

####################
# Helper functions #
####################


def get_locator(context, page_attr):
    page_attr = transform_string_to_page_attr(page_attr)
    return getattr(context.page, page_attr)


def transform_string_to_page_attr(string):
    return string.lower().replace(' ', '_')