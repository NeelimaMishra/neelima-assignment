""" This python file contains positive test case for Signin component/page """

import pytest

from globals import creds_conf

signin_creds = creds_conf["LoginCreds"]


class TestSigninCases(object):
    """This class contains test cases for User Signin"""

    @pytest.mark.smoke
    @pytest.mark.authentication
    def test_verify_user_signin_with_valid_credentials(
        self, signin_object, dashboard_object
    ):
        """This method include test case for
        # Verify that user is able to sign in successfully by providing valid credentials.
        """
        email = signin_creds["email"]
        user_password = signin_creds["password"]

        log.info("Enter valid email and valid password")
        signin_object.signin(email=email, password=user_password)
        dashboard_object.validate_signin_to_ui_successful(email)


@pytest.mark.usefixtures("signin_with_default_credential")
class TestSignoutCases(object):

    @pytest.mark.authentication
    def test_verify_user_signout(
        self, signout_object, signin_object, dashboard_object
    ):
        """This method include test case for
        # Verify that user is able to log out successfully.
        """
        email = creds_conf["LoginCreds"]["email"]
        dashboard_object.validate_signin_to_ui_successful(email)
        signout_object.signout(email=email)
        dashboard_object.validate_finance_text_not_present()
        dashboard_object.driver_obj.open_url()
        signin_object.validate_sign_in_visible()
