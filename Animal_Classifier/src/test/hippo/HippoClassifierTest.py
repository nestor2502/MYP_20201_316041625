#from hippo.src.main.HippoClassifier import *
import os.path
import sys

dir = os.path.dirname(__file__)

class_path =os.path.join(dir,"../../main/hippo")
imgs_path =os.path.join(dir,"./image_test")

sys.path.insert(0,class_path)

from HippoClassifier import HippoClassifier

import unittest
#Class of unit test to identify an hippo

class HippoClassifierTest(unittest.TestCase):


    #method that compare a hippo to elephant
    def test_compareElephant(self):
        elephant_image = os.path.join(imgs_path,"elephant.jpg")
        is_hippo = True
        clasifier = HippoClassifier()
        is_hippo = clasifier.classify(elephant_image)
        self.assertEqual(False, is_hippo)

    #method that compare a hippo to crocodile
    def test_compareCrocodile(self):
        crocodile_image = os.path.join(imgs_path,"crocodile.jpg")
        is_hippo = True
        clasifier = HippoClassifier()
        is_hippo = clasifier.classify(crocodile_image)
        self.assertEqual(False, is_hippo)

    #method that compare a hippo to rinho
    def test_compareRinho(self):
        rinho_image = os.path.join(imgs_path,"rinho.jpg")
        is_hippo = True
        clasifier = HippoClassifier()
        is_hippo = clasifier.classify(rinho_image)
        self.assertEqual(False, is_hippo)

    #method that compare a hippo to any object
    #in this case we compare a hippo to ballon
    def test_compareObject(self):
        object_image = os.path.join(imgs_path,"ballon.jpg")
        clasifier = HippoClassifier()
        is_hippo = clasifier.classify(object_image)
        self.assertEqual(False, is_hippo)

    #method that compar a hippo to hippo
    def test_compareHippo(self):
        hippo_image = os.path.join(imgs_path,"hippo12.jpg")
        is_hippo = True
        clasifier = HippoClassifier()
        is_hippo = clasifier.classify(hippo_image)
        self.assertEqual(True, is_hippo)

if __name__ == '__main__':
	unittest.main()
