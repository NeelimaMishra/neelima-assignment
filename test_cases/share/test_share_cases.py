""" This python file contains positive test case for Share component/page """

import pyperclip3
import pytest
import requests

from test_cases import test_data


@pytest.mark.usefixtures("signin_with_default_credential")
class TestShareCases(object):
    """This class contains test cases for share component"""

    @pytest.mark.share
    def test_share_stock(
        self,
        dashboard_object,
        watchlist_portfolio_object,
        search_object,
        share_object,
    ):
        """This method include test case for
        # Verify that user is able to share stock/fund link.
        """
        dashboard_object.click_main_menu()
        dashboard_object.click_home()
        search_object.search_stock(list_name=test_data.TEST_STOCK_SYMBOL2)
        watchlist_portfolio_object.click_stock_tab_inside_watchlist_listbox()
        watchlist_portfolio_object.click_stock_in_listbox(
            stock_symbol=test_data.TEST_STOCK_SYMBOL2
        )
        expected_url = share_object.driver_obj.get_current_url()
        share_object.click_share()

        if not headless:
            share_object.click_copy_link()
            expected_url = share_object.driver_obj.get_current_url()
            copied_url = pyperclip3.paste().decode()
        else:
            copied_url = share_object.get_share_link_from_dom()
            response = requests.head(
                "http://" + copied_url, allow_redirects=True
            )
            copied_url = response.url

        share_object.driver_obj.open_url(url=copied_url)
        assert expected_url == share_object.driver_obj.get_current_url(), (
            f"Copied url not same as expected url {expected_url} "
            f"Actual: {share_object.driver_obj.get_current_url()}"
        )
