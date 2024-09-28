""" This python file contains test case for Market trends component/page """

import copy

import pytest

from constants import common


@pytest.mark.usefixtures("signin_with_default_credential")
class TestMarketTrendsCases(object):
    """This class contains test cases for Market trends component"""

    @pytest.mark.markettrends
    def test_explore_market_trends_by(
        self, dashboard_object, market_trends_object
    ):
        """This method include test case for
        # Verify tabs present under Explore market trends
        """
        dashboard_object.click_main_menu()
        market_trends_object.click_market_trends()

        actual_market_trends = (
            market_trends_object.explore_market_trends_option()
        )
        expected_market_trends = copy.deepcopy(common.MARKET_TRENDS)
        for market_trend in actual_market_trends:
            if market_trend in expected_market_trends:
                expected_market_trends.remove(market_trend)
        assert (
            len(expected_market_trends) == 0
        ), f"{expected_market_trends} market trend NOT visible"
