import csv
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

