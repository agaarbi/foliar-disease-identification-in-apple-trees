# foliar-disease-identification
Identify the category of foliar disease in apple trees


# Problem Statement
Plant care and diagnosis of plants is a time consuming and expensive work. Misdiagnosis is a major problem which may lead to loss of growth and usage of wrong chemicals. Also, while inspecting for disease you also need an experienced and well trained staff to correctly identify disease and take decision accordingly.

Currently, disease diagnosis is based on human scouting which as mentioned is a time consuming work load and inefficient. To cater this problem, a diseases detecting application can be highly useful in detecting and make automated decisions.

# Setup Guide
Data -> you will need to download images data to train your model from this link https://drive.google.com/drive/folders/1_OqKAxASFk1VYgGAJqnheKEab6KP32bn?usp=sharing , if you dont have access to this link please email us at siraj@cipherslab.com

P.S. It is not necessary for you to download images and train the model as we have also uploaded pretrained model in this repo. 

To run the application, run file main.py located in app folder with uvicorn server and from postman you can send a sample image on localhost:PORT/input/
![FastAPI Working with image as input](https://user-images.githubusercontent.com/18510632/111150840-69c21f00-85b0-11eb-8f0c-9f0f4af7a665.png)


# Docker Guide
Our docker image is having little bit of trouble at this moment so it might give you an error, we will resolve the issue and update it soon.

