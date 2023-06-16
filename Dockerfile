FROM python:3.10-slim-bullseye
COPY ./requirements.txt /quote_microservice/requirements.txt
WORKDIR /quote_microservice
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /quote_microservice
EXPOSE 80
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]