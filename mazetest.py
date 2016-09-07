import unittest
import random
import turtle
from Maze import *

class testMaze(unittest.TestCase):
    def setUp(self):
        #This checks for a maze class
        self.m=Maze()
        
    def testMazeExists(self):
        pass
    
    def testScreenExists(self):
        assert type(self.m) == Maze

if __name__=="__main__":
    unittest.main(exit=False)


