import os.path
#import Hippo
import unittest
#Class of unit test to identify an hippo

class HippoClassifierTest(unittest.TestCase):

    #currently only check if the path exist
    def test_checkPath(self):
        exist_path = False
        path = "path.jpg" #this path doesn't exist
        #Hippo.check_path()
        #if path.exists(path):
            #exist_path = true
        self.assertEqual(True,exist_path)

    #method that compare a hippo to elephant
    def test_compareElephant(self):
        elephant_image = "path"
        is_hippo = True
        #is_hippo = Hippo.isHippo()
        self.assertEqual(False, is_hippo)

    #method that compare a hippo to any object
    #in this case we compare a hippo to ballon
    def test_compareObject(self):
        object_image = "path"
        is_hippo = True
        #is_hippo = Hippo.isHippo()
        self.assertEqual(False, is_hippo)

    #method that compar a hippo to hippo
    def test_compareHippo(self):
        hippo_image = "path"
        is_hippo = False
        #is_hippo = Hippo.isHippo()
        self.assertEqual(True, is_hippo)

if __name__ == '__main__':
	unittest.main()
