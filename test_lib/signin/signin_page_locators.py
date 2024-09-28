class SigninPageWebElement(object):
    """This class returns web element for the page"""

    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    @property
    def sign_in(self):
        return self.driver_obj.find_visible_element(
            locator=SigninPageLocators.XPATH_SIGN_IN
        )

    @property
    def email(self):
        return self.driver_obj.find_visible_element(
            locator=SigninPageLocators.XPATH_EMAIL
        )

    @property
    def next(self):
        return self.driver_obj.find_visible_element(
            locator=SigninPageLocators.XPATH_NEXT
        )

    @property
    def password(self):
        return self.driver_obj.find_visible_element(
            locator=SigninPageLocators.XPATH_PASSWORD
        )

    @property
    def not_now(self):
        return self.driver_obj.find_visible_element(
            locator=SigninPageLocators.XPATH_NOT_NOW
        )

    @property
    def not_now_present(self):
        return self.driver_obj.is_element_displayed(
            locator=SigninPageLocators.XPATH_NOT_NOW
        )

    @property
    def sign_in_visible(self):
        return self.driver_obj.is_element_displayed(
            locator=SigninPageLocators.XPATH_SIGN_IN
        )


class SigninPageLocators:
    """This class contains locators for signin flow"""

    XPATH_SIGN_IN = "(//span[text()='Sign in'])[1]"
    XPATH_EMAIL = "//input[@id='identifierId']"
    XPATH_NEXT = "//span[text()='Next']"
    XPATH_PASSWORD = "//input[@type='password']"
    XPATH_NOT_NOW = "//span[text()='Not now']"


class SignoutPageWebElement(object):
    """This class returns web element for the page"""

    def __init__(self, driver_obj):
        self.driver_obj = driver_obj

    def google_account(self, email):
        return self.driver_obj.find_visible_element(
            locator=SignoutPageLocators.XPATH_GOOGLE_ACCOUNT.format(email)
        )

    @property
    def signout_button(self):
        return self.driver_obj.find_visible_element(
            locator=SignoutPageLocators.XPATH_SIGNOUT
        )


class SignoutPageLocators:
    """This class contains locators for signout flow"""

    XPATH_GOOGLE_ACCOUNT = "//a[contains(@aria-label, '{}')]"
    XPATH_SIGNOUT = "//div[text()='Sign out']"
    XPATH_ACCOUNT_IFRAME = "//iframe[@name='account']"
