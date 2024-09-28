""" This python file contains positive test case for Follow component/page """

import pytest

from test_cases import test_data


@pytest.mark.usefixtures("signin_with_default_credential")
class TestFollowCases(object):
    """This class contains test cases for follow component"""

    @pytest.mark.follow
    def test_follow_stock(
        self,
        dashboard_object,
        watchlist_portfolio_object,
        search_object,
        follow_object,
    ):
        """This method include test case for
        # Verify that user is able to follow a stock/fund successfully
        """
        dashboard_object.click_main_menu()
        dashboard_object.click_home()
        search_object.search_stock(list_name=test_data.TEST_STOCK_SYMBOL2)
        watchlist_portfolio_object.click_stock_tab_inside_watchlist_listbox()
        watchlist_portfolio_object.click_stock_in_listbox(
            stock_symbol=test_data.TEST_STOCK_SYMBOL2
        )

        follow_object.click_follow()

        dashboard_object.click_main_menu()
        dashboard_object.click_default_watchlist()

        watchlist_portfolio_object.verify_stock_added_to_watchlist(
            stock_symbol=test_data.TEST_STOCK_SYMBOL2
        )

        watchlist_portfolio_object.hover_over_stock_name_and_delete_it_from_watchlist(
            stock_symbol=test_data.TEST_STOCK_SYMBOL2
        )
