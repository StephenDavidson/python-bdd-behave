import os, time

import faker, splinter
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

    # Initialize browser and add driver to global context
    context.browser = splinter.Browser(driver_name=os.getenv('BROWSER', 'firefox'))


@capture
def after_scenario(context, scenario):
    # Take screenshot if scenario fails
    if scenario.status == 'failed':
        scenario_error_dir = os.path.join(context.artifacts_dir, 'feature_errors')
        make_dir(scenario_error_dir)
        scenario_file_path = os.path.join(scenario_error_dir, scenario.feature.name.replace(' ', '_')
                                          + '_' + time.strftime("%H%M%S_%d_%m_%Y")
                                          + '.jpg')
        context.browser.driver.save_screenshot(scenario_file_path)

    context.browser.quit()


def make_dir(dir):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(dir):
        os.makedirs(dir)