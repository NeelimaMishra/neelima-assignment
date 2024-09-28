from retry import retry
from selenium.common.exceptions import TimeoutException

from test_lib.base_lib import GuiBaseLib
from test_lib.market_trends.market_trends_page_locators import (
    MarketTrendsLocators,
    MarketTrendsWebElement,
)


class MarketTrends(GuiBaseLib):

    def __init__(self):
        GuiBaseLib.__init__(self)
        self.page_obj = MarketTrendsWebElement(self.driver_obj)

    @retry(exceptions=TimeoutException, tries=2, delay=5)
    def click_market_trends(self):
        """This method click on the Market trends button"""
        log.info("Click Market trends button")
        self.driver_obj.click_element(self.page_obj.market_trends)

    @retry(exceptions=TimeoutException, tries=2, delay=5)
    def explore_market_trends_option(self):
        """This method return all the elements for explore market trends"""
        trend_element_list = self.driver_obj.find_elements_by_xpath(
            MarketTrendsLocators.XPATH_EXPLORE_MARKET_TRENDS_TABLIST
        )
        return [trend.text for trend in trend_element_list]
