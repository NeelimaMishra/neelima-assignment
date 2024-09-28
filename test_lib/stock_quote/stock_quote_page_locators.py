class QuoteWebElement(object):
    """This class returns web element for the Quote page"""

    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    def stock_data(self):
        return self.driver_obj.get_text(locator=QuoteLocators.XPATH_STOCK_DATA)

    @property
    def stock_up(self):
        return self.driver_obj.find_elements_by_xpath(
            locator=QuoteLocators.XPATH_STOCK_UP
        )

    @property
    def stock_down(self):
        return self.driver_obj.find_elements_by_xpath(
            locator=QuoteLocators.XPATH_STOCK_DOWN
        )


class QuoteLocators:
    """This class contains locators for Quote page"""

    XPATH_STOCK_DATA = "//div[@data-last-price]"
    XPATH_STOCK_UP = (
        "//div[@data-last-price]//span[contains(@aria-label, 'Up ')]"
    )
    XPATH_STOCK_DOWN = (
        "//div[@data-last-price]//span[contains(@aria-label, 'Down ')]"
    )


class ShareWebElement(object):
    """This class returns web element for Share feature"""

    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    @property
    def share_button(self):
        return self.driver_obj.find_visible_element(
            locator=ShareLocators.XPATH_SHARE
        )

    @property
    def copy_link(self):
        return self.driver_obj.find_visible_element(
            locator=ShareLocators.XPATH_COPY_LINK
        )

    @property
    def copy_link_from_dom(self):
        return self.driver_obj.get_text(
            locator=ShareLocators.XPATH_COPY_LINK_FROM_DOM
        )


class ShareLocators:
    """This class contains locators for Follow component"""

    XPATH_SHARE = "//span[text()='Share']"
    XPATH_COPY_LINK = "//span[text()='Copy link']"
    XPATH_COPY_LINK_FROM_DOM = "//div[contains(text(), 'g.co/finance')]"


class FollowWebElement(object):
    """This class returns web element for Follow feature"""

    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    @property
    def follow_button(self):
        return self.driver_obj.find_visible_element(
            locator=FollowLocators.XPATH_FOLLOW
        )


class FollowLocators:
    """This class contains locators for Follow component"""

    XPATH_FOLLOW = "//div[text()='Follow']"
