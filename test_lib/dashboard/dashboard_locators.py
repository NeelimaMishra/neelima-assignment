class DashboardWebElement(object):
    """This class returns web element for the Dashboard page"""

    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    def user_name_after_signin(self, email):
        return self.driver_obj.is_element_displayed(
            locator=DashboardLocators.XPATH_USER_AFTER_SIGNIN.format(email)
        )

    def finance_text(self):
        return self.driver_obj.is_element_displayed(
            locator=DashboardLocators.XPATH_FINANCE_TEXT
        )

    @property
    def main_menu(self):
        return self.driver_obj.find_visible_element(
            locator=DashboardLocators.XPATH_MAIN_MENU
        )

    @property
    def home(self):
        return self.driver_obj.find_visible_element(
            locator=DashboardLocators.XPATH_HOME
        )

    @property
    def create_watchlist(self):
        return self.driver_obj.find_visible_element(
            locator=DashboardLocators.XPATH_CREATE_WATCHLIST
        )

    @property
    def default_watchlist(self):
        return self.driver_obj.find_visible_element(
            locator=DashboardLocators.XPATH_DEFAULT_WATCHLIST
        )

    @property
    def create_new_list(self):
        return self.driver_obj.find_visible_element(
            locator=DashboardLocators.XPATH_CREATE_NEW_LIST_NAME
        )

    @property
    def create_new_list_save_button(self):
        return self.driver_obj.find_visible_element(
            locator=DashboardLocators.XPATH_CREATE_NEW_LIST_SAVE_BUTTON
        )

    def click_list_button_present_inside_main_menu(self, list_name):
        return self.driver_obj.find_visible_element(
            locator=DashboardLocators.XPATH_LIST_NAME_ON_MAIN_MENU.format(
                list_name
            )
        )

    def list_name_validation(self, list_name):
        return self.driver_obj.is_element_displayed(
            locator=DashboardLocators.XPATH_LIST_NAME_ON_MAIN_MENU.format(
                list_name
            )
        )

    # Portfolio
    @property
    def create_portfolio(self):
        return self.driver_obj.find_visible_element(
            locator=DashboardLocators.XPATH_CREATE_PORTFOLIO
        )

    @property
    def create_new_portfolio(self):
        return self.driver_obj.find_visible_element(
            locator=DashboardLocators.XPATH_CREATE_NEW_PORTFOLIO_NAME
        )


class DashboardLocators:
    """This class contains locators for Dashboard page"""

    XPATH_USER_AFTER_SIGNIN = "//a[contains(@aria-label, '{}')]"
    XPATH_FINANCE_TEXT = "(//a[@aria-label='Finance'])[1]"

    XPATH_MAIN_MENU = "//div[@aria-label='Main menu']"
    XPATH_HOME = "//div[text()='Home']"
    XPATH_CREATE_WATCHLIST = "//button[@aria-label='Create watchlist']"
    XPATH_DEFAULT_WATCHLIST = "//a[@title='Watchlist']"
    XPATH_CREATE_NEW_LIST_NAME = "//span[text()='List name']/following::input"
    XPATH_CREATE_NEW_LIST_SAVE_BUTTON = "//span[text()='Save']"
    XPATH_LIST_NAME_ON_MAIN_MENU = "//a[@title='{}']"

    XPATH_CREATE_PORTFOLIO = "//button[@aria-label='Create portfolio']"
    XPATH_CREATE_NEW_PORTFOLIO_NAME = (
        "//span[text()='Portfolio name']/following::input"
    )


class SearchWebElement(object):
    """This class returns web element for the Search component"""

    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    @property
    def search_for_stocks_etfs_more(self):
        return self.driver_obj.find_visible_element(
            locator=SearchLocators.XPATH_SEARCH
        )

    @property
    def no_matches(self):
        return self.driver_obj.is_element_displayed(
            locator=SearchLocators.XPATH_NO_MATCHES
        )


class SearchLocators:
    """This class contains locators for Search component"""

    XPATH_SEARCH = "//input[@aria-label='Search for stocks, ETFs & more']"
    XPATH_NO_MATCHES = (
        "//div[text()='No matches...' and @aria-live='assertive']"
    )
