import os

import yaml

from test_lib.selenium_operations import SeleniumOperations
from utility.exception_handler import log_exception_and_retry

config_file_path = os.path.abspath("config/credentials.yaml")
with open(config_file_path) as fd:
    config_data = yaml.safe_load(fd)


class GuiBaseLib:
    def __init__(self):
        self.driver = None
        self.driver_obj = None
        self.initialize_method()

    @log_exception_and_retry
    def initialize_method(self):
        """This method is to initialize sel obj and driver"""
        self.driver_obj = SeleniumOperations()
        if self.driver_obj.driver:
            self.driver = self.driver_obj.driver
            self.driver_obj.maximize_browser_window()
            self.driver.get(config_data["URL"])
