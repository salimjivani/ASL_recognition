import cv2
import numpy as np
from tensorflow import keras
from keras.models import load_model
from PIL import Image

model = keras.models.load_model('D:/Grad/CSCE 5214 Soft dev for AI/ASL_recognition-1/ASL_dataset_Model weights/ASL_Model_Weights.h5')
#model = load_model('ASL_Model_Weights.h5')
pred_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for j in range(0,26):
    img = cv2.imread('D:/Grad/CSCE 5214 Soft dev for AI/ASL_recognition-1/ASL_dataset_Model weights/Test_Images/'+pred_list[j]+'_test.jpg')
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgs = cv2.resize(img, (28,28), interpolation = cv2.INTER_CUBIC)
    imgs = imgs.reshape(-1,28,28,3)
    imgs = np.array(imgs)
    imgs = imgs.astype('float32')/255.0
    pred = model.predict_classes(imgs)
    print(pred_list[pred[0]])
