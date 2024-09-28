""" This python file contains test case for watchlist and portfolio component/page """

import pytest

from constants import common
from test_cases import test_data


@pytest.mark.usefixtures("signin_with_default_credential")
class TestWatchlistPortfolioCases(object):
    """This class contains test cases for watchlist and portfolio component"""

    @pytest.mark.watchlist
    def test_create_and_add_a_stock_to_watchlist(
        self, new_watchlist, watchlist_portfolio_object, dashboard_object
    ):
        """This method include test case for
        # Verify that create watchlist is working.
          And add a stock/investment to watchlist is working.
        """
        dashboard_object.click_main_menu()
        dashboard_object.validate_list_create_successful(
            list_name=new_watchlist
        )
        dashboard_object.click_list_present_inside_main_menu(
            list_name=new_watchlist
        )
        watchlist_portfolio_object.validate_investment_count_in_watchlist(
            list_name=new_watchlist, count=test_data.ZERO_INVESTMENT_COUNT
        )
        watchlist_portfolio_object.click_add_investments(
            list_name=new_watchlist
        )
        stock_name = test_data.TEST_STOCK_SYMBOL
        watchlist_portfolio_object.send_data_to_investment_box(
            investment_name=stock_name
        )
        watchlist_portfolio_object.click_stock_tab_inside_watchlist_listbox()
        watchlist_portfolio_object.click_stock_in_listbox(
            stock_symbol=stock_name
        )
        watchlist_portfolio_object.validate_investment_count_in_watchlist(
            list_name=new_watchlist, count=test_data.QUANTITY
        )
        watchlist_portfolio_object.verify_stock_added_to_watchlist(
            stock_symbol=stock_name
        )

    @pytest.mark.watchlist
    def test_delete_watchlist_with_stock_present(
        self, new_watchlist, watchlist_portfolio_object, dashboard_object
    ):
        """This method include test case for
        # Verify that delete watchlist is working
        """
        dashboard_object.click_main_menu()
        dashboard_object.validate_list_create_successful(
            list_name=new_watchlist
        )

        dashboard_object.click_list_present_inside_main_menu(
            list_name=new_watchlist
        )
        watchlist_portfolio_object.validate_investment_count_in_watchlist(
            list_name=new_watchlist, count=test_data.ZERO_INVESTMENT_COUNT
        )

        watchlist_portfolio_object.click_add_investments(
            list_name=new_watchlist
        )

        stock_name = test_data.TEST_STOCK_SYMBOL
        watchlist_portfolio_object.send_data_to_investment_box(
            investment_name=stock_name
        )
        # watchlist_portfolio_object.click_on_type_an_investments_name_text_box()
        # watchlist_portfolio_object.type_an_investment_name(investment_name=stock_name)

        watchlist_portfolio_object.click_stock_tab_inside_watchlist_listbox()

        watchlist_portfolio_object.click_stock_in_listbox(
            stock_symbol=stock_name
        )

        # Verify investment count after adding to Watchlist
        watchlist_portfolio_object.validate_investment_count_in_watchlist(
            list_name=new_watchlist, count=test_data.QUANTITY
        )
        watchlist_portfolio_object.verify_stock_added_to_watchlist(
            stock_symbol=stock_name
        )

        # Hover over the stock and remove it
        watchlist_portfolio_object.hover_over_stock_name_and_delete_it_from_watchlist(
            stock_symbol=stock_name
        )
        watchlist_portfolio_object.delete_watchlist(
            watchlist_name=new_watchlist, dashboard_object=dashboard_object
        )

    @pytest.mark.portfolio
    def test_add_investment_to_portfolio(
        self, new_portfolio, watchlist_portfolio_object, dashboard_object
    ):
        """This method include test case for
        # Verify that adding an investment to portfolio is working
        """
        watchlist_portfolio_object.add_investment_to_portfolio(
            new_portfolio, dashboard_object
        )
        watchlist_portfolio_object.verify_stock_added_to_portfolio(
            stock_symbol=test_data.TEST_STOCK_SYMBOL
        )
        watchlist_portfolio_object.set_currency_to_usd(dashboard_object)
        watchlist_portfolio_object.validate_portfolio_data()

    @pytest.mark.smoke
    @pytest.mark.portfolio
    def test_update_currency(
        self, new_portfolio, watchlist_portfolio_object, dashboard_object
    ):
        """This method include test case for
        # Verify that user able to update the currency for Portfolio
        """
        watchlist_portfolio_object.add_investment_to_portfolio(
            new_portfolio, dashboard_object
        )
        watchlist_portfolio_object.verify_stock_added_to_portfolio(
            stock_symbol=test_data.TEST_STOCK_SYMBOL
        )
        watchlist_portfolio_object.set_currency_to_usd(dashboard_object)
        watchlist_portfolio_object.validate_currency_name(
            portfolio=new_portfolio, currency=common.CURRENCY_CODE_1
        )
        watchlist_portfolio_object.set_currency_to_inr(dashboard_object)
        watchlist_portfolio_object.validate_currency_name(
            portfolio=new_portfolio, currency=common.CURRENCY_CODE_2
        )
