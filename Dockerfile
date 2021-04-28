FROM tensorflow/tensorflow

RUN pip install fastapi uvicorn
RUN pip install opencv-python
RUN pip install keras
RUN pip install python-multipart

RUN apt-get update && \
    apt-get install libgl1-mesa-glx -y

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
