FROM python:3
ADD requirements.txt /
RUN pip install -r requirements.txt
COPY . .
ADD main.py /
CMD [ "python", "./main.py" ]