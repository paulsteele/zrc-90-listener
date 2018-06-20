FROM python

WORKDIR /zrc-90-listener

RUN apt-get update && apt-get install -y python-pip

RUN pip install requests

COPY  ./zrc-90-listener.py ./zrc-90-listener.py

CMD ["python", "zrc-90-listener.py"]
