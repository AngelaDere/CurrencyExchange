FROM python:3.9.9-slim

# Copy necessary files
COPY settings/settings.txt /app/settings.txt
COPY exchanger_project/exchanger.py /app/exchanger.py
COPY exchanger_project/csv_with_timer.py /app/csv_with_timer.py
COPY exchanger_project/current_results.py /app/current_results.py

# Install Python libraries
RUN apt-get update
RUN pip install requests

# Set environment variables
ENV PYTHONPATH=/app

# Run code
CMD . /app/settings.txt && python3 /app/exchanger.py
