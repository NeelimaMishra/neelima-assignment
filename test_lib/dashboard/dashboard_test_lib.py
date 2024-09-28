import time

from retry import retry
from selenium.common.exceptions import TimeoutException

from constants import duration
from test_lib.base_lib import GuiBaseLib
from test_lib.dashboard.dashboard_locators import (
    DashboardLocators,
    DashboardWebElement,
    SearchLocators,
    SearchWebElement,
)


class Dashboard(GuiBaseLib):

    def __init__(self):
        GuiBaseLib.__init__(self)
        self.page_obj = DashboardWebElement(self.driver_obj)

    def validate_signin_to_ui_successful(self, email):
        """This method will verify signin successful"""
        assert self.page_obj.user_name_after_signin(
            email
        ), "Signin NOT worked for user"

    def validate_finance_text_not_present(self):
        """This method will verify finance text not present"""
        assert not self.page_obj.finance_text(), "Finance text VISIBLE"

    def click_finance_text(self):
        """This method will click on finance text"""
        assert not self.page_obj.finance_text(), "Finance text VISIBLE"

    def click_main_menu(self):
        """This method click on the Main menu button present on the left side top corner"""
        log.info("Click Main menu button")
        self.click_finance_text()
        self.driver_obj.click_element(self.page_obj.main_menu)

    def click_home(self):
        """This method click on the Home button present inside Main menu"""
        log.info("Click Home button")
        self.driver_obj.click_element(self.page_obj.home)

    def click_default_watchlist(self):
        """This method click on the default watchlist present inside Main menu"""
        log.info("Click default watchlist present inside main menu")
        self.driver_obj.click_element(self.page_obj.default_watchlist)

    @retry(exceptions=TimeoutException, tries=2, delay=5)
    def click_create_watchlist_button(self):
        """This method click on the Create watchlist button present inside Main menu"""
        log.info("Click create watchlist button")
        self.driver_obj.click_element(self.page_obj.create_watchlist)

    @retry(exceptions=TimeoutException, tries=2, delay=5)
    def create_new_list_name_text_box(self, list_name: str):
        """THis method enter list name in Create a new list text box"""
        log.info("Enter list name: " + list_name)
        self.driver_obj.send_keys(self.page_obj.create_new_list, list_name)

    def click_create_new_list_save_button(
        self, delay=duration.SHORT_WAIT_TIME
    ):
        """This method click on the save button present inside the create new list form"""
        log.info("Click save button present inside the create new list form")
        self.driver_obj.click_element(
            self.page_obj.create_new_list_save_button
        )
        """
        This is a bug.
        The element is present and the click also succeeded but portfolio creation fails
        if this delay is not introduced
        """
        time.sleep(delay)

    def click_list_present_inside_main_menu(self, list_name):
        """
        This method click on the list(Either Watchlist or Portfolio)
        button present inside Main menu
        """
        log.info("Click list button present inside Main menu")
        self.driver_obj.click_element(
            self.page_obj.click_list_button_present_inside_main_menu(list_name)
        )

    def validate_list_create_successful(self, list_name):
        """This method will verify list created successfully"""
        assert self.page_obj.list_name_validation(
            list_name
        ), f"list {list_name} NOT created"

    def validate_list_delete_successful(self, list_name):
        """This method will verify list deleted successfully"""
        assert not self.page_obj.list_name_validation(
            list_name
        ), "list NOT deleted"

    @retry(exceptions=TimeoutException, tries=2, delay=5)
    def click_create_portfolio_button(self):
        """This method click on the Create portfolio button present inside Main menu"""
        log.info("Click create portfolio button")
        self.driver_obj.is_element_displayed(
            DashboardLocators.XPATH_CREATE_PORTFOLIO
        )
        time.sleep(duration.SHORT_WAIT_TIME)
        self.driver_obj.click_element(self.page_obj.create_portfolio)

    @retry(exceptions=TimeoutException, tries=2, delay=1)
    def create_new_portfolio_name_text_box(self, list_name: str):
        """THis method enter portfolio name in Create a new list text box"""
        log.info("Enter portfolio name: " + list_name)
        self.driver_obj.send_enter_keys(self.page_obj.create_new_portfolio)
        self.driver_obj.send_keys(
            self.page_obj.create_new_portfolio, list_name, ctrla=True
        )


class Search(GuiBaseLib):

    def __init__(self):
        GuiBaseLib.__init__(self)
        self.page_obj = SearchWebElement(self.driver_obj)

    def search_stock(self, list_name: str):
        """This method enter stock or eft in the search box"""
        log.info("Enter name: " + list_name)
        element = self.click_search_box()
        self.driver_obj.send_keys(element, list_name)

    def click_search_box(self):
        element_list = self.driver_obj.find_elements_by_xpath(
            SearchLocators.XPATH_SEARCH
        )
        element = self.driver_obj.find_visible_element_from_list(
            element_list=element_list
        )
        self.driver_obj.click_element(element)
        return element

    def validate_no_matches(self):
        """This method will verify no matches for investment name"""
        assert self.page_obj.no_matches, "No matches NOT displayed"
