import os
import requests
from csv_with_timer import *
from current_results import *


class ExchangeRate:
    """Verify current exchange rate."""
    def __init__(self):
        self.api = os.environ['API']
        self.api_key = os.environ['API_KEY']

    @save_results_with_runtime
    def exchange_rate_usdpln(self):
        parameters = {"access_key": self.api_key}
        try:
            request = requests.get(self.api, params=parameters)
        except TimeoutError as e:
            return "Timeout! " + str(e)

        usdpln_value = request.json()['quotes']['USDPLN']
        return usdpln_value


if __name__ == '__main__':
    print(print_current_results())
