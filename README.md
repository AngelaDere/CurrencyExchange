### Description
This project checks current US Dollar Polish Zloty rate and saves result to csv file.
The program also saves information about time the code is started and the runtime.

### Requirements
* Python 3.8+
* Docker

### Usage
* Clone this git repository
* `cd` into the root directory of the repo

### Build docker image
* Run `docker image build -t python-exchanger .`

### Run docker image as a container
* Run `docker run --name python-exchanger-container python-exchanger`

### Obtain csv file
* Run `docker cp python-exchanger-container:/app/usdpln.csv .`
