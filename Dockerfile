FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN python -m pip install tensorflow-cpu==2.3.0rc2
RUN python -m pip install Keras==2.4.3
RUN python -m pip install opencv-python

COPY ./app /app
