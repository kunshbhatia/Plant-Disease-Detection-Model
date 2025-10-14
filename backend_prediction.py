import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import tensorflow
import numpy as np
import re

classes = []
with open("data.txt", "r") as file:
    content = file.readlines()
    for i in content:
        classes.append(i[0:-1])

def format_result(result,prediction):
    result = classes[prediction]
    result = " ".join(re.sub(r'[^a-zA-Z]', ' ', result).split()).upper()
    return result

def prediction_plant(file):
    model =  tensorflow.keras.models.load_model("model.keras")
    img = tensorflow.keras.preprocessing.image.load_img(file,target_size=(128,128))
    final_img = np.array([img])
    prediction = model.predict(final_img)
    prediction = np.argmax(prediction)
    result = classes[prediction]
    return format_result(result,prediction)