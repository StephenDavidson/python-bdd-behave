import os, time
import faker, splinter

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from splinter.driver.webdriver import BaseWebDriver, WebDriverElement

from behave.log_capture import capture

import config

@capture
def before_all(context):

    # Add fake factory
    context.fake = faker.Faker()

    # Add logging
    context.config.setup_logging()

    # Add base url from config
    context.base_url = config.url

    # Dir to output test artifacts
    context.artifacts_dir = 'artifacts'

@capture
def before_scenario(context, scenario):

    browser_name = os.getenv('BROWSER', 'chrome')
    if browser_name == 'chrome' and os.getenv('HEADLESS') == 'true':
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        browser = BaseWebDriver()
        browser.driver = Chrome(chrome_options=options)
        browser.element_class = WebDriverElement
    else:
        browser = splinter.Browser(driver_name=browser_name)

    # Initialize browser and add driver to global context
    context.browser = browser


@capture
def after_scenario(context, scenario):
    # Take screenshot if scenario fails
    if scenario.status == 'failed':
        scenario_error_dir = os.path.join(context.artifacts_dir, 'feature_errors')
        make_dir(scenario_error_dir)
        scenario_file_path = os.path.join(scenario_error_dir, scenario.feature.name.replace(' ', '_')
                                          + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                          + '.png')
        context.browser.driver.save_screenshot(scenario_file_path)

    context.browser.quit()


def make_dir(dir):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
