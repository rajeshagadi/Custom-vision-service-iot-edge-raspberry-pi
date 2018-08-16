FROM resin/raspberrypi3-python:2.7

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends libboost-python1.55.0 && \
    rm -rf /var/lib/apt/lists/* 

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN useradd -ms /bin/bash moduleuser
USER moduleuser

ENTRYPOINT [ "python", "-u", "./main.py" ]
