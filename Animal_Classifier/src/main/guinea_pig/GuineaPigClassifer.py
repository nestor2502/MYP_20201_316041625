from tensorflow import keras
from matplotlib import pyplot

import sys
import os

dir = os.path.dirname(__file__)

classifier_path =os.path.join(dir,"../")
preprocess_path = os.path.join(dir,"../../tools")
h5_path = os.path.join(dir, '../../training')

sys.path.insert(0,classifier_path)
sys.path.insert(0,preprocess_path)
sys.path.insert(0,h5_path)

from Classifier import Classifier
from Preprocess import Preprocess

import pickle
import os
import numpy as np

class GuineaPig(Classifier):
    
    def __init__(self):
        pass

    def __threeBlocks_model(self):
        """ Model proposal for neuronal network """

        model = keras.Sequential()

        model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(60, 60, 1)))
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(keras.layers.Dropout(0.25))

        model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(keras.layers.Dropout(0.25))

        model.add(keras.layers.Conv2D(128, (3, 3), activation='relu'))
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(keras.layers.Dropout(0.25))

        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(128, activation='relu',kernel_initializer='he_uniform'))
        model.add(keras.layers.Dropout(0.5))
        model.add(keras.layers.Dense(2, activation='softmax'))

        model.compile(optimizer='adam' , loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        return model

    def training(self,images_path,labels_path,repetitions):
        """ Read training images and labels. Train the neuronal network with model and save
            model in .h5 file. This method only execute when user want to re-train the
            network with other images and labels
        """

        if not os.path.isfile(images_path) or not os.path.isfile(labels_path):

            raise ValueError("arguments doesn't files")
            
        train_images = pickle.load(open(images_path,"rb"))

        train_labels = pickle.load(open(labels_path,"rb"))

        new_model = self.__threeBlocks_model()

        new_model.fit(np.array(train_images), np.array(train_labels), batch_size=32, epochs=repetitions)

        new_model.save(os.path.join(h5_path,"guineapig.h5"))

    def classify(self,img_test):
        """ Execute the model of neuronal network and return true if the image is a 
            guinea pig.

            Args:
                img_mdf(numpy array). Array of image data

            Returns:
                True. If the max value of precitions is guinea pig
        """

        save_path = os.path.join(h5_path,"guineapig.h5")

        preprocess = Preprocess()

        img = preprocess.prepare_image(img_test,60)

        if not os.path.exists(save_path):
            raise FileExistsError("File guineapig.h5 was deleted. :(")

        model = keras.models.load_model(save_path)

        predictions = model.predict(img)

        max = np.argmax(predictions)

        categories = ["guinea pig","not guinea pig"]

        result = categories[max]

        if (result == "guinea pig"):
            return True
        else:
            return False

    


