FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim-2021-10-02

ENV DEBIAN_FRONTEND=noninteractive

COPY ./requirements.txt /home/requirements.txt
RUN pip3 install -r /home/requirements.txt

COPY . /home/

WORKDIR /home
EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]