FROM python:3.11-buster

WORKDIR /framework

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "pytest" ]
CMD [ ". -s -v" ]
