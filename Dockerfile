FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt
RUN export FLASK_APP=routes

COPY . /app

ENTRYPOINT [ "flask" ]

CMD ["run"]
