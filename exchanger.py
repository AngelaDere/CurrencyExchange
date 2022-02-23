import os
import csv
import requests
import time
from datetime import datetime
from pathlib import Path


def save_results_with_runtime(method):
    """Calculate how long code was running. Save results to csv file."""
    def calculate(*args, **kwargs):
        csv_file = Path('/app/usdpln.csv')
        if not csv_file.is_file():
            with open(csv_file, 'w', newline='') as file:
                header = [
                    'DATE',
                    'HOUR',
                    'USD/PLN',
                    'RUNTIME'
                ]
                writer = csv.writer(file)

                # write the header
                writer.writerow(header)

        with open(csv_file, 'a', newline='') as file:
            start = datetime.now()
            current_value = method(*args, **kwargs)
            end = datetime.now()
            time_difference = end - start

            data = [
                start.date(),
                '%02d:%02d:%02d' % (start.hour, start.minute, start.second),
                current_value,
                time_difference
            ]

            writer = csv.writer(file)

            # write the row
            writer.writerow(data)

        return current_value
    return calculate


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
