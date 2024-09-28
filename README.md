# Introduction

Selenium is a browser automation tool. Page Object Model has been used for this Python Selenium pytest framework. 
This particular "assignment" only covers Selenium setup and GUI automation for Python based programming language.

---
# Coverage Approach

- Identify Core Functional Areas
   - Search functionality: Test stock query in the search bar.
   - Stock data direction: Ensure that the correct stock movement direction is displayed for stock symbols.
   - Login/authentication: Ensure signin/signout flow works properly.
   - Watchlist CRUD operation.
   - Portfolio CRUD operation along with portfolio value validation after adding investments to it.
   - Share a stock page link
   - Currency change should reflect change in currency on portfolio value.

- Coverage Goals
   - Due to limited bandwidth we aim for at least coverage of all core features (search, stock load, market trends,
     display Currency, portfolio, watchlist) and basic operations and prioritize high-traffic and critical paths.

- Automation trigger using CI Jenkins
   - Smoke markers are implemented and a run_smoke.sh is provided at project level which can be used to triggered
     smoke suite.

- Browser Support
   - Although this assignment has been tested on only Chrome browser, we also provided a support to run on firefox as
     an input argument "--browser" for pytest

- Error Handling:
   - Decorators are used for error handling in library methods which ensure cleaner code and also make our
     code more resilient to glitches in UI and network issues during validation runs.
---

# Directory Structure

- frontend-automation
   - config: Configuration/credentials file.
   - constants: Contains constant used throughout file.
   - test_cases: Contains pytest test suites/cases.
   - test_cases/test_data: Contains test data used in the project.
   - test_lib: Contains python libraries related to all components, core lib and Selenium operations.
   - test_lib/locators: Contains element locator and XPATH
   - utility: Contains scripts to setup to run pytest test scenarios, encrypt/decrypt user credential and exception handler.
   - globals: Contains globally used variables.
   - requirements: Include python, pytest & selenium modules prerequisites.

# Assumptions

Python3.11 is in system path.
chromedriver_autoinstaller is use to install selenium webdriver compatible to Chrome browser version.
However you can set your webdriver to the environment path.
The command in bash script starts with python3.11, please fell free to modify as per your setup.
The code has been tested on Chrome browser with and without headless mode.

# Pre-requisites

Run following command before running any actual test:
python3.11 -m pip install -r requirements.txt

---
# Test Run Command Using Pytest

If you want to run smoke suite with browser headless mode using pytest, run the following command.
run_smoke.sh shell script is present at the project folder level.
python3.11 -m pytest -v -s --headless true -m smoke

If you want to run entire suite with browser headless mode using pytest, run the following command.
python3.11 -m pytest -v -s --headless true

If you want to run entire suite with browser without headless mode using pytest, run the following command.
python3.11 -m pytest -v -s

If you want to run single test with browser without headless mode using pytest, run the following command.
python3.11 -m pytest -v -s -k 'test_verify_user_signin_with_valid_credentials'

If you do not need logs to be printed during execution on the console and prefer a cleaner view,
remove the -s parameter from the pytest command line.

All tests are running and have been validated at the time of submission of this assignment.
However if there are major changes to finance.google.com, it may lead to failing tests and will require changes.

---
admin@FVFZ87NELYWG assignment_keysight % ./run_smoke.sh
============================================================================= test session starts =============================================================================
platform darwin -- Python 3.11.0, pytest-8.3.3, pluggy-1.5.0 -- /usr/local/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/admin/Documents/assignment_keysight
configfile: pytest.ini
collected 12 items / 8 deselected / 4 selected                                                                                                                                

test_cases/search/test_search_cases.py::TestSearchCases::test_search_stock PASSED                                                                                       [ 25%]
test_cases/search/test_search_cases.py::TestSearchCases::test_stock_direction PASSED                                                                                    [ 50%]
test_cases/test_signin/test_signin_cases.py::TestSigninCases::test_verify_user_signin_with_valid_credentials PASSED                                                     [ 75%]
test_cases/test_watchlist_portfolio/test_watchlist_portfolio.py::TestWatchlistPortfolioCases::test_update_currency PASSED                                               [100%]

================================================================= 4 passed, 8 deselected in 298.35s (0:04:58) =================================================================
---

Credential protection: 
To protect user credential using which we login the Finance.google.com I have encrypted the creds.Cryptography module has been used for this.
key.key is currently checked in folder however this would not be the case during actual implementation.
The key for decryption should be store at a secure location such as AWS secret key location.