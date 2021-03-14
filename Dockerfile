FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN python -m pip install tensorflow

COPY ./app /app