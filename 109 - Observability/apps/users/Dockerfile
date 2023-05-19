FROM ubuntu:focal

WORKDIR /opt/app

# Install python
RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python3 python3-pip libpq5

# Install python deps
COPY requirements.txt .
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "ddtrace-run" ]
CMD [ "flask", "--app", "app.py", "run", "--host=0.0.0.0" ]

COPY app.py .
