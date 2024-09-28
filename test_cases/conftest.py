import builtins

import pytest

from globals import creds_conf
from test_lib.dashboard.dashboard_test_lib import Dashboard, Search
from test_lib.market_trends.market_trends_test_lib import MarketTrends
from test_lib.selenium_operations import SeleniumOperations
from test_lib.signin.signin_test_lib import Signin, Signout
from test_lib.stock_quote.stock_quote_test_lib import Follow, Quote, Share
from test_lib.watchlist_portfolio.watchlist_portfolio_test_lib import WatchlistPortfolio
from utility import utilities as utils
from utility.utilities import initialize_logger

builtins.log = initialize_logger()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Type in browser: chrome or firefox",
    )
    parser.addoption(
        "--headless",
        action="store",
        default="false",
        help="Run browser in headless mode: true or false",
    )


def pytest_configure(config):
    builtins.test_browser = config.getoption("--browser")
    builtins.headless = config.getoption("--headless").lower() == "true"


@pytest.fixture(autouse=True, scope="class")
def setup():
    log.info("Executing Setup")
    global obj
    obj = SeleniumOperations(create_new_driver_instance=True)


@pytest.fixture(autouse=True, scope="session")
def teardown():
    yield
    obj.quit_browser()


@pytest.fixture(scope="function")
def signin_object():
    return Signin()


@pytest.fixture(scope="class")
def signin_object_class():
    return Signin()


@pytest.fixture(scope="function")
def signout_object():
    return Signout()


@pytest.fixture(scope="function")
def dashboard_object():
    return Dashboard()


@pytest.fixture(scope="function")
def search_object():
    return Search()


@pytest.fixture(scope="function")
def follow_object():
    return Follow()


@pytest.fixture(scope="function")
def share_object():
    return Share()


@pytest.fixture(scope="function")
def market_trends_object():
    return MarketTrends()


@pytest.fixture(scope="function")
def quote_object():
    return Quote()


@pytest.fixture(scope="function")
def watchlist_portfolio_object():
    return WatchlistPortfolio()


@pytest.fixture(scope="function")
def new_watchlist(dashboard_object, watchlist_portfolio_object):
    watchlist_name = utils.generate_random_watchlist_name()
    dashboard_object.click_main_menu()
    dashboard_object.click_create_watchlist_button()
    dashboard_object.create_new_list_name_text_box(list_name=watchlist_name)
    dashboard_object.click_create_new_list_save_button()
    dashboard_object.driver.refresh()
    dashboard_object.click_main_menu()
    dashboard_object.click_home()
    yield watchlist_name
    watchlist_portfolio_object.delete_watchlist(
        watchlist_name, dashboard_object
    )


@pytest.fixture(scope="class")
def signin_with_default_credential(signin_object_class):
    email = creds_conf["LoginCreds"]["email"]
    user_password = creds_conf["LoginCreds"]["password"]
    signin_object_class.signin(email=email, password=user_password)


@pytest.fixture(scope="function")
def new_portfolio(dashboard_object, watchlist_portfolio_object):
    portfolio_name = utils.generate_random_portfolio_name()
    dashboard_object.click_main_menu()
    dashboard_object.click_create_portfolio_button()
    dashboard_object.create_new_portfolio_name_text_box(
        list_name=portfolio_name
    )
    dashboard_object.click_create_new_list_save_button()
    # There is a bug in UI where clicking on menu sidebar immediately after creating a portfolio
    # causes the menu(side pane) hamburger button to be in a wierd state.
    # Refreshing the page as a workaround.
    # We can log a bug on Google finance team! This is manually reproducible.
    dashboard_object.driver.refresh()
    yield portfolio_name
    watchlist_portfolio_object.delete_portfolio(
        list_name=portfolio_name, dashboard_object=dashboard_object
    )
