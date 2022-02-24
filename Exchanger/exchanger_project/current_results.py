import time
from datetime import datetime
from exchanger import ExchangeRate


def print_current_results():
    """Run code for 15 seconds and show results on the screen."""
    i = 0
    while i < 5:
        print(
            "TIME: ",
            datetime.now(),
            " CURRENT RATE: ",
            ExchangeRate().exchange_rate_usdpln()
        )
        time.sleep(3)
        i += 1
