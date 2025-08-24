FROM python:latest
ARG VERSION=9.2.1

RUN wget https://adafruit-circuit-python.s3.amazonaws.com/bin/mpy-cross/linux-amd64/mpy-cross-linux-amd64-${VERSION}.static -O /bin/mpycross
RUN chmod +x /bin/mpycross

WORKDIR /app

COPY ./src /app/src
COPY ./build.sh /bin/build.sh

RUN mkdir -p /app/build && rm -rf /app/build/*
RUN chmod +x /bin/build.sh

ENTRYPOINT ["/bin/build.sh"]

