FROM python:3.8.4-slim-buster
COPY main.py /
COPY lectorapi.py /
COPY sensors.py /
COPY requirements.txt /

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload
