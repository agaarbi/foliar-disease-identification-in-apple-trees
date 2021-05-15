import csv
import shutil

import tensorflow as tf
import cv2
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import numpy as np
import uuid


json_file = open('model_json.json','r')


loaded_model_json = json_file.read()
json_file.close()



loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights('model_weights.h5')
loaded_model.compile(optimizer='adam',
                  loss = 'categorical_crossentropy',
                  metrics=['categorical_accuracy'])

IMAGE_PATH = "C:/Users/siraj/Downloads/plant-pathology-2020/images/"
TRAIN_PATH="C:/Users/siraj/Work/foliar-disease-identification/data/train.csv"


#loading images
def load_image(loaded_image):
    image = cv2.imread(loaded_image)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#my_image = load_image('Train_99.jpg')


def process(img):
    return cv2.resize(img/255.0, (512, 512)).reshape(-1, 512, 512, 3)
def predict(img):
    return loaded_model.layers[2](loaded_model.layers[1](loaded_model.layers[0](process(img)))).numpy()[0]


def modelRun(file):
    #img = cv2.cvtColor(np.array(file), cv2.COLOR_BGR2RGB)
    # above line will be used and below line will be commented out if using Image
    #img = process(file)
    resultOfPrediction = predict(file)
    resultInArgMax = resultOfPrediction.argmax()
    
    if(resultInArgMax==0):
       return "Healthy"
    elif(resultInArgMax==1):
        return "Multiple"
    elif(resultInArgMax==2):
        return "Rust"
    elif(resultInArgMax==3):
        return "Scab"
    else:
        return "WTF"


def modelRunLoc(file):
    img = load_image(file)
    resultOfPrediction = predict(img)
    resultInArgMax = resultOfPrediction.argmax()
    
    if(resultInArgMax==0):
       return "Healthy"
    elif(resultInArgMax==1):
        return "Multiple Diseases"
    elif(resultInArgMax==2):
        return "Rust"
    elif(resultInArgMax==3):
        return "Scab"
    else:
        return "Invalid"


#preds = predict(my_image)
#print(preds)

#print(modelRun("Train_99.jpg"))
#print(modelRun("Train_80.jpg"))
        
        
###############################################################################
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


@app.post("/input/")

async def predictAPI(file: UploadFile = File(...)):
    content = await file.read()
    nparr = np.fromstring(content, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    myImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = modelRun(myImage)
    id = uuid.uuid4().hex[:8]
    file.filename = "Train_" + id + ".jpg"


    file_location = IMAGE_PATH+"/"+file.filename
    with open(file_location, 'wb') as file_object:  #saving user input image for future retraining model
        file_object.write(content)



    if(result=="Healthy"):
        fields = [file.filename, 1, 0,0,0]
    elif(result=="Scab"):
        fields = [file.filename, 0, 0, 0, 1]
    elif(result=="Multiple Diseases"):
        fields = [file.filename, 0, 1, 0, 0]
    elif(result=="Rust"):
        fields = [file.filename, 0, 0, 1, 0]

    with open(fr'{TRAIN_PATH}', 'a') as f:  #saving the outcome to train.csv for future retraining
        writer = csv.writer(f)
        writer.writerow(fields)
    return result


@app.get("/predict/loc")
def predictFromLoc ():
    return modelRunLoc("Train_99.jpg")

@app.get("/")
async def root():
    return {"message": "Working"}
###############################################################################





