class WatchlistPortfolioPageWebElement(object):
    """This class returns web element for the page"""

    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    def add_investments_button(self, list_name):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_ADD_INVESTMENTS.format(
                list_name
            )
        )

    @property
    def type_an_investment_name_text_box(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_TYPE_AN_INVESTMENT_NAME_BOX
        )

    @property
    def click_stock_button_inside_listbox(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_STOCK_TAB_INSIDE_WATCHLIST_LISTBOX
        )

    def click_stock_present_in_listbox(self, stock_symbol):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_STOCK_NAME_IN_LISTBOX.format(
                stock_symbol
            )
        )

    def stock_after_added_to_watchlist(self, stock_symbol):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_STOCK_AFTER_ADDED_TO_WATCHLIST.format(
                stock_symbol
            )
        )

    def stock_added_in_watchlist(self, stock_symbol):
        """This method returns the locator for stock name so that we can hover over it"""
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_STOCK_AFTER_ADDED_TO_WATCHLIST.format(
                stock_symbol
            )
        )

    @property
    def close_button_to_remove_stock_name_from_watchlist(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_CLOSE_BUTTON_TO_REMOVE_STOCK_FROM_WATCHLIST
        )

    @property
    def more_menu_options(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_MORE_MENU_OPTIONS
        )

    @property
    def click_on_delete_in_more_menu_options(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_DELETE_IN_MORE_MENU_OPTIONS
        )

    @property
    def click_on_delete_this_list_button(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_DELETE_THIS_LIST_BUTTON
        )

    @property
    def delete_portfolio(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_DELETE_PORTFOLIO
        )

    def watchlist_count_updated(self, list_name, count):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_WATCHLIST_INVESTMENT_COUNT.format(
                list_name, count
            )
        )

    def check_stock_list_after_enter_in_search(self, stock_symbol):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_STOCK_NAME_IN_LISTBOX.format(
                stock_symbol
            )
        )

    # Portfolio
    def check_add_investment_portfolio_button(self, list_name):
        return self.driver_obj.find_elements_by_xpath(
            locator=WatchlistPortfolioPageLocators.XPATH_ADD_INVESTMENT_PORTFOLIO.format(
                list_name
            )
        )

    @property
    def symbol_text_box_for_portfolio(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_INVESTMENT_NAME_OR_SYMBOL_FOR_PORTFOLIO
        )

    def portfolio_count_value(self, list_name, count):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_PORTFOLIO_INVESTMENT_COUNT.format(
                list_name, count
            )
        )

    @property
    def quantity(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_QUANTITY
        )

    @property
    def purchase_date(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_PURCHASE_DATE
        )

    @property
    def purchase_price(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_PURCHASE_PRICE
        )

    def stock_name_after_add_to_portfolio(self, stock_symbol):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_STOCK_AFTER_ADDED_TO_PORTFOLIO.format(
                stock_symbol
            )
        )

    @property
    def expand_more_option_investment(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_INVESTMENT_EXPAND_MORE
        )

    @property
    def change_currency(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_CHANGE_CURRENCY
        )

    @property
    def check_currency_in_usd(self):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_UPDATE_CURRENCY_USD
        )

    @property
    def check_currency_in_inr(self):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_UPDATE_CURRENCY_INR
        )

    @property
    def currency_in_inr(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_UPDATE_CURRENCY_INR
        )

    def check_currency_name(self, portfolio, currency):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_CHECK_CURRENCY_NAME.format(
                portfolio, currency
            )
        )

    @property
    def update_currency_dropdown(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_UPDATE_CURRENCY_DROPDOWN
        )

    @property
    def select_usd_from_currency_dropdown(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_SELECT_UNITED_STATES_DOLLAR
        )

    @property
    def select_inr_from_currency_dropdown(self):
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_SELECT_INDIAN_RUPEE
        )

    def check_purchase_price_in_row(self, purchase_price):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_PURCHASE_PRICE_IN_ROW.format(
                purchase_price
            )
        )

    def check_quantity_in_row(self, quantity):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_QUANTITY_IN_ROW.format(
                quantity
            )
        )

    def check_date_in_row(self, expected_date):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_DATE_IN_ROW.format(
                expected_date
            )
        )

    def get_total_gain_in_row(self):
        return self.driver_obj.get_text(
            locator=WatchlistPortfolioPageLocators.XPATH_TOTAL_GAIN_IN_ROW
        )

    def get_value_in_row(self):
        return self.driver_obj.get_text(
            locator=WatchlistPortfolioPageLocators.XPATH_VALUE_IN_ROW
        )

    def stock_added_in_portfolio(self, stock_symbol):
        """This method returns the locator for stock name so that we can hover over it"""
        return self.driver_obj.find_visible_element(
            locator=WatchlistPortfolioPageLocators.XPATH_STOCK_AFTER_ADDED_TO_PORTFOLIO.format(
                stock_symbol
            )
        )

    def check_portfolio_value_after_investment_delete(self, value):
        return self.driver_obj.is_element_displayed(
            locator=WatchlistPortfolioPageLocators.XPATH_PORTFOLIO_VALUE.format(
                value
            )
        )


class WatchlistPortfolioPageLocators:
    """This class contains locators for YOUR LISTS page"""

    XPATH_ADD_INVESTMENTS = (
        "//div[@aria-label='Your lists']/following"
        "::span[text()='{}']/following::span[text()='Add investments']"
    )
    XPATH_TYPE_AN_INVESTMENT_NAME_BOX = (
        "//input[@aria-label='Type an investment name or symbol']"
    )
    XPATH_STOCK_TAB_INSIDE_WATCHLIST_LISTBOX = "//div[@data-tab-id='stocks']"
    XPATH_STOCK_NAME_IN_LISTBOX = "//div[@data-hinttext='NASDAQ: {}']"
    XPATH_STOCK_AFTER_ADDED_TO_WATCHLIST = (
        "//div[@class='ZCC9mc']//div[text()='{}']"
    )
    XPATH_CLOSE_BUTTON_TO_REMOVE_STOCK_FROM_WATCHLIST = (
        "//div[@class='ZCC9mc']//child::*[text()='close']"
    )
    XPATH_MORE_MENU_OPTIONS = "(//button[@aria-label='More menu options'])[1]"
    XPATH_DELETE_IN_MORE_MENU_OPTIONS = "(//span[text()='Delete'])[1]"
    XPATH_DELETE_THIS_LIST_BUTTON = "(//span[text()='Delete'])[3]"
    XPATH_WATCHLIST_INVESTMENT_COUNT = (
        "//div[@aria-label='Your lists']"
        "/following::span[text()='{}']"
        "/following-sibling::div[text()='{}']"
    )
    XPATH_DELETE_PORTFOLIO = (
        "//div[text()='Delete this portfolio?']/parent::div/following-sibling::div/div/div//div/"
        "following-sibling::span[text()='Delete']"
    )

    # Portfolio
    XPATH_ADD_INVESTMENT_PORTFOLIO = (
        "//div[text()='Nothing in this portfolio yet']"
        "/parent::div/child::div/button"
        "/span[text()='Add investments']"
    )
    XPATH_INVESTMENT_NAME_OR_SYMBOL_FOR_PORTFOLIO = (
        "//input[@aria-label='Type an investment name or symbol']"
    )
    XPATH_PORTFOLIO_INVESTMENT_COUNT = (
        "//div[@aria-label='Your lists']"
        "/following::span[text()='{}']"
        "/following-sibling::div[text()='{}']"
    )
    XPATH_QUANTITY = (
        "//label[text()='Quantity']/parent::div/child::div/div/div"
        "/label/span/following-sibling::input[@type='number']"
    )
    XPATH_PURCHASE_DATE = (
        "//label[text()='Purchase date']/parent::div"
        "/child::div/div/div/div/div/div/input[@type='text']"
    )
    XPATH_PURCHASE_PRICE = (
        "//label[text()='Purchase price']/parent::div"
        "/child::div/label/span/following-sibling::input[@type='number']"
    )

    XPATH_STOCK_AFTER_ADDED_TO_PORTFOLIO = (
        "(//c-wiz/following::div[text()='SYMBOL']"
        "/following::div[text()='{}'])[1]"
    )

    XPATH_INVESTMENT_EXPAND_MORE = "//i[text()='expand_more']"

    # Inside more menu
    XPATH_UPDATE_CURRENCY_USD = "//li[@aria-label='Update currency: USD']"
    XPATH_CHANGE_CURRENCY = "//li[contains(@aria-label, 'Update currency: ')]"
    XPATH_CHECK_CURRENCY_NAME = (
        "(//div[text()='{}']/parent::div/parent::div"
        "/following-sibling::div/child::div/c-wiz"
        "/div//div//div[@data-currency-code='{}'])[1]"
    )
    XPATH_UPDATE_CURRENCY_INR = "//li[@aria-label='Update currency: INR']"
    # Update currency menu
    XPATH_CURRENCY_INR = ""
    XPATH_UPDATE_CURRENCY_DROPDOWN = "//span[@aria-label='']"
    XPATH_SELECT_INDIAN_RUPEE = "//span[text()='Indian Rupee']"
    XPATH_SELECT_UNITED_STATES_DOLLAR = "//span[text()='United States Dollar']"

    # Row validation
    XPATH_PURCHASE_PRICE_IN_ROW = (
        "//div[text()='Purchase price']/parent::div"
        "/following-sibling::div/child::div"
        "/following-sibling::div/child::span/div/div[text()='{}']"
    )
    XPATH_QUANTITY_IN_ROW = (
        "//div[text()='Quantity']/parent::div/following-sibling::div"
        "/child::div[text()='{}']"
    )
    XPATH_DATE_IN_ROW = (
        "//div[text()='Purchase date']/parent::div"
        "/following-sibling::div/child::div[text()='{}']"
    )
    XPATH_TOTAL_GAIN_IN_ROW = (
        "//div[text()='Total gain']/parent::div"
        "/following-sibling::div/div/div/span/div/div"
    )
    XPATH_VALUE_IN_ROW = (
        "//div[text()='Total gain']/parent::div"
        "/following-sibling::div/div/div/div/div/span"
    )
    XPATH_PORTFOLIO_VALUE = "(//div[text()='{}'])[1]"
