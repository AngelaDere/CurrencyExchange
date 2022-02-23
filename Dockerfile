FROM python:3.9.9-slim

# Copy necessary files
COPY settings.txt /app/settings.txt
COPY exchanger.py /app/exchanger.py

# Install Python libraries
RUN apt-get update
RUN pip install requests

# Set environment variables
ENV PYTHONPATH=/app

# Run code
CMD . /app/settings.txt && python3 /app/exchanger.py
