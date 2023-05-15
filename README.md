# How to run this scraper

1. Install Python (pip, virtualenv), Git

2. Clone repository from [git](https://github.com/ebrahim-j/beem_africa_assessment.git)

3. Create a virtual environemt. Instructions [here](https://realpython.com/lessons/creating-virtual-environment/)

4. Change directory into the location of the cloned repository.

4. Activate environment and install requirements using command `pip install -r requirements.txt`

5. Create a folder called `output_data` under the `section_a` folder

6. Run the file using command `python section_a\mcc_scraper.py`


# Dockerize the scraper

1. Install and Run Docker

2. Build the container image using command `docker build -t mnc_mcc_scraper .`

3. Start your container `docker run mcc_mnc_scraper`. (You should see the output logs of the scraper, as well as a new output file generated at `section_a/output_data`)

4. To access the docker image from Docker hub, pull images using command `docker pull ebrahimj/mcc_mnc_scraper`
