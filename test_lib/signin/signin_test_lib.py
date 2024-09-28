from test_lib.base_lib import GuiBaseLib
from test_lib.signin.signin_page_locators import (
    SigninPageWebElement,
    SignoutPageLocators,
    SignoutPageWebElement,
)
from utility.exception_handler import log_exception_and_retry


class Signin(GuiBaseLib):

    def __init__(self):
        GuiBaseLib.__init__(self)
        self.page_obj = SigninPageWebElement(self.driver_obj)

    def signin(self, email: str, password: str):
        log.info("Click Signin button")
        self.driver_obj.click_element(self.page_obj.sign_in)
        self.enter_email(email=email)
        self.click_next()
        self.enter_password(password=password)
        log.info("Click Next button after entering password in Login flow")
        self.click_next()
        if self.page_obj.not_now_present:
            self.driver_obj.click_element(self.page_obj.not_now)
        return self.driver_obj

    def enter_email(self, email: str):
        log.info("Enter Email: " + email)
        self.driver_obj.send_keys(self.page_obj.email, email)

    def enter_password(self, password: str):
        log.info("Enter Password")
        self.driver_obj.send_keys(self.page_obj.password, password)

    def click_next(self):
        log.info("Click Next button")
        self.driver_obj.click_element(self.page_obj.next)

    def validate_sign_in_visible(self):
        """This method will verify sign in button displayed"""
        assert self.page_obj.sign_in_visible, "SIGN IN NOT displayed"


class Signout(GuiBaseLib):

    def __init__(self):
        GuiBaseLib.__init__(self)
        self.page_obj = SignoutPageWebElement(self.driver_obj)

    @log_exception_and_retry
    def signout(self, email):
        """This method sign out from Google account"""
        self.click_google_account(email)
        self.click_signout()
        return self.driver_obj

    def click_google_account(self, email):
        log.info("Click google account button")
        self.driver_obj.click_element(self.page_obj.google_account(email))

    def click_signout(self):
        self.driver_obj.click_in_iframe(
            SignoutPageLocators.XPATH_SIGNOUT,
            SignoutPageLocators.XPATH_ACCOUNT_IFRAME,
        )
