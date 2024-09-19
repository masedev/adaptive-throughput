FROM python:3.9

ADD client.py client.py

COPY utils/* utils/

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN python main.py
