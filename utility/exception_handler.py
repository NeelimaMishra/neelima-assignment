import inspect
import logging
import traceback

from retry import retry
from selenium.common.exceptions import TimeoutException, WebDriverException

# Set up basic logging configuration
logging.basicConfig(level=logging.ERROR)


def log_exception_and_retry(func):
    @retry(tries=3, delay=5, exceptions=WebDriverException)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (TimeoutException, WebDriverException, AssertionError) as e:
            # Log the full traceback along with exception details
            frame = inspect.trace()[-1]
            logging.error(f"Exception occurred in function: {func.__name__}")
            logging.error(
                f"Exception occurred at {frame.filename}, line {frame.lineno}"
            )
            logging.error(
                "Traceback:\n"
                + "".join(traceback.format_exception(None, e, e.__traceback__))
            )

            # Refresh the page
            driver_obj = args[0].driver_obj
            driver_obj.refresh()

            raise e  # Re-raise the original exception

    return wrapper
