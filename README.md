# foliar-disease-identification
Identify the category of foliar disease in apple trees


# Problem Statement
Plant care and diagnosis of plants is a time consuming and expensive work. Misdiagnosis is a major problem which may lead to loss of growth and usage of wrong chemicals. Also, while inspecting for disease you also need an experienced and well trained staff to correctly identify disease and take decision accordingly.

Currently, disease diagnosis is based on human scouting which as mentioned is a time consuming work load and inefficient. To cater this problem, a diseases detecting application can be highly useful in detecting and make automated decisions.

# Setup Guide
Data -> you will need to download images data to train your model from this link https://drive.google.com/drive/folders/1_OqKAxASFk1VYgGAJqnheKEab6KP32bn?usp=sharing , if you dont have access to this link please email us at siraj@cipherslab.com

P.S. It is not necessary for you to download images and train the model as we have also uploaded pretrained model in this repo. 

# PHASE II

# FAST-API
To run the application, run file main.py located in app folder with uvicorn server and from postman you can send a sample image on localhost:PORT/input/
![FastAPI Working with image as input](https://user-images.githubusercontent.com/18510632/111150840-69c21f00-85b0-11eb-8f0c-9f0f4af7a665.png)



# EDA

To preview EDA and model training, go to app/EDA/eda.ipynb and open file with google collab. you can also train your own model with your own hyperparameters using this file but you will need to download images data from the drive link provided above.

<img width="767" alt="screenshot1" src="https://user-images.githubusercontent.com/18510632/111152564-ad1d8d00-85b2-11eb-880f-73a4e17eeaa7.PNG">
<img width="772" alt="screenshot2" src="https://user-images.githubusercontent.com/18510632/111152568-ae4eba00-85b2-11eb-848a-26f7b8c7ff9f.PNG">
<img width="765" alt="screenshot3" src="https://user-images.githubusercontent.com/18510632/111152569-ae4eba00-85b2-11eb-916d-e334507bf5c4.PNG">
<img width="770" alt="screenshot4" src="https://user-images.githubusercontent.com/18510632/111152570-aee75080-85b2-11eb-8480-1061bf93b26a.PNG">
<img width="775" alt="screenshot5" src="https://user-images.githubusercontent.com/18510632/111152572-af7fe700-85b2-11eb-9510-97826a4b4471.PNG">
<img width="761" alt="screenshot6" src="https://user-images.githubusercontent.com/18510632/111152573-af7fe700-85b2-11eb-908e-46e0fa86e826.PNG">
<img width="768" alt="screenshot7" src="https://user-images.githubusercontent.com/18510632/111152574-b0187d80-85b2-11eb-96a9-4f17f43a7072.PNG">



# Docker Guide
Port Expose is 80

Packages Installed
-tensorflow base image
-fastapi
-uvicorn
-opencv
-keras




# PHASE III


# DOCKER RUNNING ON LOCAL MACHINE

![Dockers container working](https://user-images.githubusercontent.com/18510632/116822723-eaa59c00-ab99-11eb-8ad3-9d0323c04d2e.png)

# DOCKER ON CLOUD

Our docker image running on cloud

![WhatsApp Image 2021-05-02 at 23 01 41](https://user-images.githubusercontent.com/18510632/116823029-7a981580-ab9b-11eb-9009-c4c660c32819.jpeg)

Hitting our endpoint on cloud address to get model classification result

![Dockerandpostman](https://github.com/Iamsiraj/foliar-disease-identification/blob/staging/screenshots/Postman%20and%20Cloud.png)


# ML-FLOW

![WhatsApp Image 2021-04-23 at 04 14 05](https://user-images.githubusercontent.com/18510632/116823072-d5ca0800-ab9b-11eb-82e7-b9cdba953002.jpeg)

NOTE: Due to limitation of our personal computers and no GPUs, we could not able to train whole model in our local machine while using Ml-flow.

# DAGSTER PIPELINE

Our current implementation of pipeline is a proof of concept where the model will get trained. In phase IV, we will further implement to save the training model in docker volume and another pipeline will fetch the model to load it and identify disease. For this course, we will save every image recieved from user and its predicted outcome to docker volume and use these new images to further retrain our model through dagster pipeline. The better approach would be to involve human dependency in identifying if identified disease by model is correct or not and then retrain the model but due to limited time resource we have omitted this step.

![WhatsApp Image 2021-05-02 at 22 23 21](https://user-images.githubusercontent.com/18510632/116822961-27be5e00-ab9b-11eb-8aa8-4267a6817e05.jpeg)
![WhatsApp Image 2021-05-02 at 22 35 07](https://user-images.githubusercontent.com/18510632/116822965-2b51e500-ab9b-11eb-88f2-2951f3c88f9f.jpeg)
![WhatsApp Image 2021-05-02 at 22 35 26](https://user-images.githubusercontent.com/18510632/116822971-2e4cd580-ab9b-11eb-8a64-146a1a12d82a.jpeg)

NOTE: Due to limitation of our personal computers and no GPUs, we could not able to train whole model in our local machine while using dagster and Ml-flow. 

# PRUNING

![WhatsApp Image 2021-05-02 at 22 23 21](https://github.com/Iamsiraj/foliar-disease-identification/blob/staging/screenshots/Prunning%20Model%20Accuracy.png)





