from retry import retry

from test_lib.base_lib import GuiBaseLib
from test_lib.stock_quote.stock_quote_page_locators import (
    FollowWebElement,
    QuoteLocators,
    QuoteWebElement,
    ShareWebElement,
)
from utility.exception_handler import log_exception_and_retry


class Quote(GuiBaseLib):

    def __init__(self):
        GuiBaseLib.__init__(self)
        self.page_obj = QuoteWebElement(self.driver_obj)

    def check_stock_data(self):
        """This method get the stock data"""
        data = self.driver_obj.get_text(locator=QuoteLocators.XPATH_STOCK_DATA)
        return data

    def check_stock_going_up_or_down(self):
        """This method will verify stock is going up or going down"""
        data = self.check_stock_data()
        change = data.split()[2]
        if "+" in change:
            assert (
                len(self.page_obj.stock_up) == 1
            ), f"Up direction not found for {change}"
        elif "-" in change:
            assert (
                len(self.page_obj.stock_down) == 1
            ), f"Down direction not found for {change}"


class Follow(GuiBaseLib):

    def __init__(self):
        GuiBaseLib.__init__(self)
        self.page_obj = FollowWebElement(self.driver_obj)

    def click_follow(self):
        """This method click on the Follow button"""
        log.info("Click follow button")
        self.driver_obj.hover_and_click(self.page_obj.follow_button)


class Share(GuiBaseLib):

    def __init__(self):
        GuiBaseLib.__init__(self)
        self.page_obj = ShareWebElement(self.driver_obj)

    @log_exception_and_retry
    def click_share(self):
        """This method click on the Share button"""
        log.info("Click share button")
        self.driver_obj.hover_and_click(self.page_obj.share_button)

    def click_copy_link(self):
        """This method click on the copy link button"""
        log.info("Click copy link button")
        self.driver_obj.hover_and_click(self.page_obj.copy_link)

    @retry(tries=3, delay=5, exceptions=AssertionError)
    def get_share_link_from_dom(self):
        """
        Since google finance webpage copy sharable link does not support headless runs,
        we will test by reading sharable link directly from DOM id headless=True
        """
        share_url = self.page_obj.copy_link_from_dom
        if not share_url:
            assert False, "Shared url empty. Retrying.."
        return share_url
