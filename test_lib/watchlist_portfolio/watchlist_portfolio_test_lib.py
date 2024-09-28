from retry import retry
from selenium.common.exceptions import TimeoutException

from constants import duration
from test_cases import test_data
from test_lib.base_lib import GuiBaseLib
from test_lib.watchlist_portfolio.watchlist_portfolio_locators import (
    WatchlistPortfolioPageLocators,
    WatchlistPortfolioPageWebElement,
)
from utility.exception_handler import log_exception_and_retry
from utility.utilities import date_formatter, sanitize_price


class WatchlistPortfolio(GuiBaseLib):
    """This class contains Watchlist and Portfolio methods"""

    def __init__(self):
        GuiBaseLib.__init__(self)
        self.page_obj = WatchlistPortfolioPageWebElement(self.driver_obj)

    @log_exception_and_retry
    def validate_investment_count_in_watchlist(self, list_name, count):
        """This method will verify watchlist created successfully"""
        element_list = self.driver_obj.find_elements_by_xpath(
            WatchlistPortfolioPageLocators.XPATH_WATCHLIST_INVESTMENT_COUNT.format(
                list_name, count
            )
        )
        element = self.driver_obj.find_visible_element_from_list(
            element_list=element_list
        )
        assert self.driver_obj.is_displayed(
            element
        ), f"Investment count: {count} is not visible in Watchlist: {list_name}"

    def click_add_investments(self, list_name):
        """Click add investment button"""
        log.info("Click + Add investments button")
        self.driver_obj.click_element(
            self.page_obj.add_investments_button(list_name)
        )

    def send_data_to_investment_box(self, investment_name):
        element_list = self.driver_obj.find_elements_by_xpath(
            WatchlistPortfolioPageLocators.XPATH_TYPE_AN_INVESTMENT_NAME_BOX
        )
        element = self.driver_obj.find_visible_element_from_list(
            element_list=element_list
        )
        self.driver_obj.click_element(element)
        self.driver_obj.send_keys(element, investment_name)

    def click_on_type_an_investments_name_text_box(self):
        """This method click on Type an investments text box"""
        log.info("Click on Type an investments text box")
        self.driver_obj.click_element(
            self.page_obj.type_an_investment_name_text_box
        )

    def type_an_investment_name(self, investment_name: str):
        """Investment name"""
        log.info("Investment name: " + investment_name)
        self.driver_obj.send_keys(
            self.page_obj.type_an_investment_name_text_box, investment_name
        )

    def click_stock_tab_inside_watchlist_listbox(self):
        """Click stock tab present inside watchlist listbox"""
        log.info("Click stock tab present inside watchlist listbox")
        self.driver_obj.click_element(
            self.page_obj.click_stock_button_inside_listbox
        )

    @retry(exceptions=TimeoutException, tries=2, delay=5)
    def click_stock_in_listbox(self, stock_symbol):
        """This method click on the stock symbol present inside list box"""
        self.driver_obj.click_element(
            self.page_obj.click_stock_present_in_listbox(stock_symbol)
        )

    def verify_stock_added_to_watchlist(self, stock_symbol):
        """This method will verify stock added successfully to watchlist or not"""
        element_list = self.driver_obj.find_elements_by_xpath(
            WatchlistPortfolioPageLocators.XPATH_STOCK_AFTER_ADDED_TO_WATCHLIST.format(
                stock_symbol
            )
        )
        element = self.driver_obj.find_visible_element_from_list(
            element_list=element_list
        )
        assert self.driver_obj.is_displayed(
            element
        ), f"Stock: {stock_symbol} not added to watchlist"

    def verify_stock_tab_inside_watchlist_listbox(self):
        """Verify stock tab not present inside watchlist listbox"""
        log.info("Verify stock tab not present inside watchlist listbox")
        assert (
            not self.page_obj.click_stock_button_inside_listbox
        ), "Stock tab PRESENT inside listbox"

    @log_exception_and_retry
    def hover_over_stock_name_and_delete_it_from_watchlist(self, stock_symbol):
        """Hover over stock name and delete it"""
        element_list = self.driver_obj.find_elements_by_xpath(
            WatchlistPortfolioPageLocators.XPATH_STOCK_AFTER_ADDED_TO_WATCHLIST.format(
                stock_symbol
            )
        )
        element = self.driver_obj.find_visible_element_from_list(
            element_list=element_list
        )
        self.driver_obj.hover(element)
        log.info(
            "Click on the close button to remove the stock from watch list"
        )

        element_list = self.driver_obj.find_elements_by_xpath(
            WatchlistPortfolioPageLocators.XPATH_CLOSE_BUTTON_TO_REMOVE_STOCK_FROM_WATCHLIST
        )
        element = self.driver_obj.find_visible_element_from_list(
            element_list=element_list
        )
        self.driver_obj.click_element(element)

    @retry(exceptions=TimeoutException, tries=2, delay=5)
    def click_more_menu_options(self):
        try:
            log.info("Click on the vertical three dots i.e. more menu options")
            self.driver_obj.hover(self.page_obj.more_menu_options)
            self.driver_obj.click_element(self.page_obj.more_menu_options)
        except TimeoutException:
            self.driver_obj.refresh()
            # re-raise exception for retry
            raise TimeoutException

    def validate_stock_shows_after_enter_in_search(self, stock_symbol):
        """This method will verify stock list in list after entering in search"""
        assert self.page_obj.check_stock_list_after_enter_in_search(
            stock_symbol
        ), f"Search is NOT working. Tried to search stock {stock_symbol}"

    def click_delete_on_more_menu_options(self):
        log.info("Click on the delete button in more menu options")
        self.driver_obj.click_element(
            self.page_obj.click_on_delete_in_more_menu_options
        )

    def click_delete_this_list_button(self):
        log.info("Click on delete this list button")
        self.driver_obj.click_element(
            self.page_obj.click_on_delete_this_list_button
        )

    @log_exception_and_retry
    def delete_watchlist(self, watchlist_name, dashboard_object):
        dashboard_object.click_main_menu()
        if dashboard_object.page_obj.list_name_validation(
            list_name=watchlist_name
        ):
            dashboard_object.click_list_present_inside_main_menu(
                list_name=watchlist_name
            )
            self.click_more_menu_options()
            self.click_delete_on_more_menu_options()
            self.click_delete_this_list_button()
            dashboard_object.validate_list_delete_successful(
                list_name=watchlist_name
            )
        else:
            dashboard_object.click_home()

    def click_delete_portfolio(self):
        log.info("Click on delete portfolio button when 0 investment present")
        self.driver_obj.click_element(self.page_obj.delete_portfolio)

    def click_add_investment_in_portfolio(self, list_name):
        log.info("Click + Add investments button present inside a portfolio")
        element_list = self.page_obj.check_add_investment_portfolio_button(
            list_name
        )
        element = self.driver_obj.find_visible_element_from_list(
            element_list=element_list
        )
        self.driver_obj.click_element(element)

    def click_on_type_an_investments_name_text_box_for_portfolio(self):
        log.info("Click on Type an investments text box for portfolio")
        self.driver_obj.click_element(
            self.page_obj.symbol_text_box_for_portfolio
        )

    def type_an_investment_name_portfolio(self, investment_name: str):
        log.info("Investment name: " + investment_name)
        self.driver_obj.send_keys(
            self.page_obj.symbol_text_box_for_portfolio, investment_name
        )

    def validate_investment_count_in_portfolio(
        self, list_name: str, count: str
    ):
        """This method will verify portfolio(count) created successfully or not"""
        assert self.page_obj.portfolio_count_value(
            list_name, count
        ), f"Investment count: {count} is not visible in Portfolio: {list_name}"

    def verify_stock_added_to_portfolio(self, stock_symbol):
        """This method will verify stock added successfully to portfolio or not"""
        assert self.page_obj.stock_name_after_add_to_portfolio(stock_symbol)

    def quantity_text_box(self):
        """This method checks the quantity text box present"""
        self.driver_obj.click_element(self.page_obj.quantity)

    def enter_quantity(self, quantity: str):
        """This method enter quantity"""
        log.info("Quantity: " + quantity)
        self.driver_obj.send_keys(self.page_obj.quantity, quantity, ctrla=True)

    def purchase_date_text_box(self):
        """This method checks the purchase date text box present"""
        self.driver_obj.click_element(self.page_obj.purchase_date)

    def enter_purchase_date(self, purchase_date: str):
        log.info("Purchase date: " + purchase_date)
        self.driver_obj.send_keys(
            self.page_obj.purchase_date, purchase_date, ctrla=True
        )

    def purchase_price_text_box(self):
        """This method checks the purchase price text box present"""
        self.driver_obj.click_element(self.page_obj.purchase_price)

    def enter_purchase_price(self, purchase_price: str):
        log.info("Purchase price: " + purchase_price)
        self.driver_obj.send_keys(
            self.page_obj.purchase_price,
            purchase_price,
            ctrla=True,
            delay=duration.DEFAULT_WAIT_TIME,
        )

    def expand_more_investment(self):
        """
        This method scroll to the element and then clicks on the
        expand more present in the investment row
        """
        self.driver_obj.scroll_to_element_and_click(
            self.page_obj.expand_more_option_investment
        )

    def validate_investment_purchase_price_in_portfolio(self, purchase_price):
        """This method will verify the investment purchase value"""
        assert self.page_obj.check_purchase_price_in_row(
            purchase_price=purchase_price
        ), f"Investment purchase price: {purchase_price} is showing INCORRECT in portfolio"

    def validate_investment_quantity_in_portfolio(self, quantity):
        """This method will verify the investment quantity"""
        assert self.page_obj.check_quantity_in_row(
            quantity=quantity
        ), f"Investment quantity: {quantity} is showing INCORRECT in portfolio"

    def get_investment_total_gain_in_portfolio(self):
        """This method will get the investment total gain"""
        return self.page_obj.get_total_gain_in_row()

    def get_investment_value_in_portfolio(self):
        """This method will get the investment value"""
        return self.page_obj.get_value_in_row()

    def portfolio_value_after_investment_delete(self, value):
        """This method will verify portfolio value after investment delete"""
        assert self.page_obj.check_portfolio_value_after_investment_delete(
            value
        ), f"Portfolio value: {value} is showing INCORRECT after an investment delete"

    @log_exception_and_retry
    def delete_portfolio(self, list_name, dashboard_object):
        dashboard_object.click_main_menu()
        if dashboard_object.page_obj.list_name_validation(list_name=list_name):
            dashboard_object.click_list_present_inside_main_menu(
                list_name=list_name
            )
            self.click_more_menu_options()
            self.click_delete_on_more_menu_options()
            self.click_delete_this_list_button()
            dashboard_object.validate_list_delete_successful(
                list_name=list_name
            )
        else:
            dashboard_object.click_home()

    def add_investment_to_portfolio(self, list_name, dashboard_object):
        dashboard_object.click_main_menu()
        dashboard_object.click_list_present_inside_main_menu(
            list_name=list_name
        )
        self.validate_investment_count_in_portfolio(
            list_name=list_name, count=test_data.ZERO_INVESTMENT_COUNT
        )
        self.click_add_investment_in_portfolio(list_name=list_name)
        self.click_on_type_an_investments_name_text_box_for_portfolio()
        self.type_an_investment_name_portfolio(
            investment_name=test_data.TEST_STOCK_SYMBOL
        )
        self.click_stock_tab_inside_watchlist_listbox()
        self.click_stock_in_listbox(stock_symbol=test_data.TEST_STOCK_SYMBOL)
        self.quantity_text_box()
        self.enter_quantity(test_data.QUANTITY)
        self.purchase_date_text_box()
        self.enter_purchase_date(purchase_date=test_data.PURCHASE_DATE)
        self.purchase_price_text_box()
        self.enter_purchase_price(
            purchase_price=sanitize_price(test_data.PURCHASE_PRICE)
        )
        dashboard_object.click_create_new_list_save_button()

    def validate_investment_date_in_portfolio(self, expected_date):
        """This method will verify the investment date"""
        assert self.page_obj.check_date_in_row(
            expected_date=expected_date
        ), f"Investment date: {expected_date} is showing INCORRECT in portfolio"

    @log_exception_and_retry
    def validate_investment_value(
        self, buy_price=test_data.PURCHASE_PRICE, buy_qty=test_data.QUANTITY
    ):
        """This method validates the portfolio total gain and value"""
        total_gain = self.get_investment_total_gain_in_portfolio()
        value = self.get_investment_value_in_portfolio()
        total_gain = float(sanitize_price(total_gain))
        value = float(sanitize_price(value))
        buy_price = float(sanitize_price(buy_price))
        buy_qty = int(sanitize_price(buy_qty))
        calculated_investment_value = (total_gain / 100) * (
            buy_price * buy_qty
        )
        tolerance = 20.0
        # Since the value continuously changes, we will allow a tolerance of 20 USD.
        # This is a judgement that a largecap stock like AAPL will very unlikely
        # have a huge move in few seconds.
        assert abs(calculated_investment_value - value) <= tolerance, (
            f"Expected investment value within {tolerance} USD of "
            f"{calculated_investment_value}, but found {value}"
        )

    @log_exception_and_retry
    def validate_portfolio_data(self):
        """
        This method validates the investment details like purchase price,
        quantity and purchase date
        """
        self.expand_more_investment()
        self.validate_investment_purchase_price_in_portfolio(
            test_data.PURCHASE_PRICE
        )
        self.validate_investment_quantity_in_portfolio(test_data.QUANTITY)
        self.validate_investment_date_in_portfolio(
            date_formatter(test_data.PURCHASE_DATE)
        )
        self.validate_investment_value()

    @log_exception_and_retry
    def set_currency_to_usd(self, dashboard_object):
        """This method sets the currency to USD"""
        self.click_more_menu_options()
        if not self.page_obj.check_currency_in_usd:
            self.driver_obj.click_element(self.page_obj.change_currency)
            self.driver_obj.hover_and_click(
                self.page_obj.update_currency_dropdown
            )
            self.driver_obj.hover_and_click(
                self.page_obj.select_usd_from_currency_dropdown
            )
            dashboard_object.click_create_new_list_save_button()
        else:
            self.click_more_menu_options()

    @log_exception_and_retry
    def set_currency_to_inr(self, dashboard_object):
        """This method set the currency to inr"""
        self.click_more_menu_options()
        if not self.page_obj.check_currency_in_inr:
            self.driver_obj.click_element(self.page_obj.change_currency)
            self.driver_obj.hover_and_click(
                self.page_obj.update_currency_dropdown
            )
            self.driver_obj.hover_and_click(
                self.page_obj.select_inr_from_currency_dropdown
            )
            dashboard_object.click_create_new_list_save_button()
        else:
            self.click_more_menu_options()

    def validate_currency_name(self, portfolio, currency):
        """This method will verify currency name/code"""
        assert self.page_obj.check_currency_name(
            portfolio, currency
        ), f"Currency is INCORRECT {currency}"
