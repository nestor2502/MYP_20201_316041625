import os.path
import sys

dir = os.path.dirname(__file__)

class_path =os.path.join(dir,"../../main/giraffe")
imgs_path =os.path.join(dir,"./")

sys.path.insert(0,class_path)

from GiraffeClassifier import Giraffe

import unittest
#Class of unit test to identify an Giraffe

class GiraffeClassifierTest(unittest.TestCase):



    #method that compare a Giraffe to emu
    def test_compareEmu(self):
        emu_image = os.path.join(imgs_path, "emu.jpg")
        is_Giraffe = False
        clasifier = Giraffe()
        is_Giraffe = clasifier.classify(emu_image)
        self.assertEqual(False, is_Giraffe)


    #method that compare a Giraffe to any object
    def test_compareObject(self):
        object_image = os.path.join(imgs_path, "ballon.jpg")
        clasifier = Giraffe()
        is_Giraffe = clasifier.classify(object_image)
        self.assertEqual(False, is_Giraffe)

    #method that compar a Giraffe to Giraffe
    def test_compareGiraffe(self):
        Giraffe_image = os.path.join(imgs_path,"ostrich.jpg")
        clasifier = Giraffe()
        is_Giraffe = clasifier.classify(Giraffe_image)
        self.assertEqual(False, is_Giraffe)

if __name__ == '__main__':
	unittest.main()
