from tensorflow import keras

import sys,os

dir = os.path.dirname(__file__)

classifier_path =os.path.join(dir,"../")
preprocess_path = os.path.join(dir,"../../tools")
h5_path = os.path.join(dir, '../../training')

sys.path.insert(0,classifier_path)
sys.path.insert(0,preprocess_path)
sys.path.insert(0,h5_path)

from Classifier import Classifier
import pickle
import os
import numpy as np
from Preprocess import Preprocess


class Giraffe(Classifier):
    
    def __init__(self):
        pass

    def __threeBlocks_model(self):
        """ Model proposal for neuronal network """

        model = keras.Sequential()

        model.add(keras.layers.Conv2D(32, (3, 3), activation='relu',
                                      input_shape=(60, 60, 1)))
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(keras.layers.Dropout(0.25))

        model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(keras.layers.Dropout(0.25))

        model.add(keras.layers.Conv2D(128, (3, 3), activation='relu'))
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(keras.layers.Dropout(0.25))

        model.add(keras.layers.Conv2D(256, (3, 3), activation='relu'))
        model.add(keras.layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(keras.layers.Dropout(0.25))

        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(256, activation='relu',
                                     kernel_initializer='he_uniform'))
        model.add(keras.layers.Dropout(0.5))
        model.add(keras.layers.Dense(2, activation='softmax'))

        model.compile(optimizer='adam' ,
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        return model

    def training(self):
        """ Read training images and labels.
        Trains the neuronal network with model and saves it in .h5 file
        """        
        train_images = pickle.load(open("giraffe_images.pickle","rb"))
        train_labels = pickle.load(open("giraffe_labels.pickle","rb"))
        new_model = self.__threeBlocks_model()

        new_model.fit(train_images, train_labels,
                      batch_size=32, epochs=150)

        save_path = os.path.join(h5_path)

        if not os.path.exists(save_path):
            print("Directory training has not been detected, creating...")
            os.mkdir(save_path)

        new_model.save(os.path.join(save_path,"giraffe.h5"))

    def classify(self,img_mdf):
        """ Execute the model of neuronal network
        Returns if the image is an giraffe.

            Args:
                img_mdf(numpy array). Array of image data

            Returns:
                True. If the max value of precitions is giraffe
        """

        save_path = os.path.join(h5_path,"giraffe.h5")

        if not os.path.exists(save_path):
            print("Invalid path")
            return

        model = keras.models.load_model(save_path)

        preprocess = Preprocess()

        img_mdf = preprocess.prepare_image(img_mdf,60)
        
        predictions = model.predict(img_mdf)

        max = np.argmax(predictions)

        categories = ["giraffe","not a giraffe"]

        result = categories[max]

        if (result == "giraffe"):
            return True
        else:
            return False




