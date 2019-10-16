
#from Ostrich.src.main.OstrichClassifier import *
import os.path
import sys

dir = os.path.dirname(__file__)

class_path =os.path.join(dir,"../../main/ostrich")
imgs_path =os.path.join(dir,"./")

sys.path.insert(0,class_path)

from OstrichClassifier import Ostrich

import unittest
#Class of unit test to identify an Ostrich

class OstrichClassifierTest(unittest.TestCase):



    #method that compare a Ostrich to emu
    def test_compareEmu(self):
        emu_image = os.path.join(imgs_path, "emu.jpg")
        is_Ostrich = False
        clasifier = Ostrich()
        is_Ostrich = clasifier.classify(emu_image)
        self.assertEqual(False, is_Ostrich)


    #method that compare a Ostrich to any object
    def test_compareObject(self):
        object_image = os.path.join(imgs_path, "ballon.jpg")
        clasifier = Ostrich()
        is_Ostrich = clasifier.classify(object_image)
        self.assertEqual(False, is_Ostrich)

    #method that compar a Ostrich to Ostrich
    def test_compareOstrich(self):
        Ostrich_image = os.path.join(imgs_path,"ostrich.jpg")
        clasifier = Ostrich()
        is_Ostrich = clasifier.classify(Ostrich_image)
        self.assertEqual(True, is_Ostrich)

if __name__ == '__main__':
	unittest.main()
