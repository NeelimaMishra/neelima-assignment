class MarketTrendsWebElement(object):
    """This class returns web element for Market trends feature"""

    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    @property
    def market_trends(self):
        return self.driver_obj.find_visible_element(
            locator=MarketTrendsLocators.XPATH_MARKET_TRENDS
        )


class MarketTrendsLocators:
    """This class contains locators for Market trends component"""

    XPATH_MARKET_TRENDS = "//i[text()='manage_search']"
    XPATH_EXPLORE_MARKET_TRENDS_TABLIST = (
        "//div[@aria-label='markets-navigation']/div/div/div/div/div/a"
    )
