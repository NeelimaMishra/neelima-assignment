""" This python file contains positive test case for search component/page """

import pytest

from test_cases import test_data


@pytest.mark.usefixtures("signin_with_default_credential")
class TestSearchCases(object):
    """This class contains test cases for search component"""

    @pytest.mark.smoke
    @pytest.mark.search
    def test_search_stock(
        self, dashboard_object, watchlist_portfolio_object, search_object
    ):
        """This method include test case for
        # Verify that user is able to search a stock/fund successfully
        """
        list_name = test_data.TEST_STOCK_SYMBOL
        dashboard_object.click_main_menu()
        dashboard_object.click_home()
        search_object.search_stock(list_name=list_name)

        watchlist_portfolio_object.validate_stock_shows_after_enter_in_search(
            stock_symbol=list_name
        )

    @pytest.mark.search
    def test_search_negative_case(
        self, dashboard_object, watchlist_portfolio_object, search_object
    ):
        """This method include test case for
        # Verify that index name should not list under stock
        """
        list_name = test_data.TEXT_INDEX_SYMBOL
        dashboard_object.click_main_menu()
        dashboard_object.click_home()
        element = search_object.click_search_box()
        watchlist_portfolio_object.click_stock_tab_inside_watchlist_listbox()
        search_object.driver_obj.send_keys(element, list_name)
        search_object.validate_no_matches()
        dashboard_object.click_main_menu()
        dashboard_object.click_home()

    @pytest.mark.smoke
    @pytest.mark.search
    def test_stock_direction(
        self,
        dashboard_object,
        search_object,
        watchlist_portfolio_object,
        quote_object,
    ):
        """This method include test case for
        # Verify that user is able to search a stock/fund successfully
        """
        list_name = test_data.TEST_STOCK_SYMBOL
        dashboard_object.click_main_menu()
        dashboard_object.click_home()
        search_object.search_stock(list_name=list_name)
        watchlist_portfolio_object.click_stock_in_listbox(
            stock_symbol=list_name
        )
        quote_object.check_stock_going_up_or_down()
