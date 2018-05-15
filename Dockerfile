FROM python:3.6
LABEL version="1.0"

COPY requirements.txt /req/
RUN pip3 install -r /req/requirements.txt

COPY consumer-twitter.py /opt/

VOLUME /work/
WORKDIR /work/

ENTRYPOINT ["python","/opt/consumer-twitter.py"]
