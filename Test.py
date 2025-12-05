#test all functions making sure they work properly
#everyone

import unittest
from FileRead import FileRead
from Matrix import matrix
from Operation import right
from Operation import left
from Operation import up
from Operation import down
from State import left_weight
from State import right_weight
from State import is_empty
from State import balance_calc
from State import con1_balance_check
from State import con2_balance_check
from State import State
from boundCheck import isEmpty, pathToNewContainer

# This tests if a file is read in correctly
class TestFileRead(unittest.TestCase):
    def test_CorrectRead(self):
        testFile = "ShipCase1.txt"
        listOfContainers = FileRead(testFile)
        self.assertEqual(len(listOfContainers), 96, "The file is not read correctly")

class TestMatrixCreation(unittest.TestCase):
    def test_CorrectRead(self):
        testFile = "operationtest.txt"
        listOfContainers = FileRead(testFile)
        m = matrix(listOfContainers, 8, 12)
        self.assertEqual(m[1][1].description, "test", "The matrix is not read correctly")

class TestOperations(unittest.TestCase):
    def test_right(self):
        testFile = "operationtest.txt"
        listOfContainers = FileRead(testFile)
        m = matrix(listOfContainers, 8, 12)
        m = right(m, 1, 1)
        des = m[1][2].description
        self.assertEqual(des, "test", "The container is not moved right correctly")

    def test_left(self):
        testFile = "operationtest.txt"
        listOfContainers = FileRead(testFile)
        m = matrix(listOfContainers, 8, 12)
        m = left(m, 1, 1)
        des = m[1][0].description
        self.assertEqual(des, "test", "The container is not moved left correctly")
    
    def test_up(self):
        testFile = "operationtest.txt"
        listOfContainers = FileRead(testFile)
        m = matrix(listOfContainers, 8, 12)
        m = up(m, 1, 1)
        des = m[2][1].description
        self.assertEqual(des, "test", "The container is not moved up correctly")

    def test_down(self):
        testFile = "operationtest.txt"
        listOfContainers = FileRead(testFile)
        m = matrix(listOfContainers, 8, 12)
        m = down(m, 1, 1)
        des = m[0][1].description
        self.assertEqual(des, "test", "The container is not moved down correctly")

class TestStates(unittest.TestCase):
    def test_lw(self):
        testFile = "operationtest.txt"
        listOfContainers = FileRead(testFile)
        m = matrix(listOfContainers, 8, 12)
        sum = left_weight(m, 8, 12)
        self.assertEqual(sum, 11111, "The left weight of the matrix is not summed correctly")

    def test_rw(self):
        testFile = "operationtest.txt"
        listOfContainers = FileRead(testFile)
        m = matrix(listOfContainers, 8, 12)
        sum = right_weight(m, 8, 12)
        self.assertEqual(sum, 20000, "The right weight of the matrix is not summed correctly")
    
    def test_is_empty(self):
        testFile = "operationtest.txt"
        listOfContainers = FileRead(testFile)
        m = matrix(listOfContainers, 8, 12)
        check = is_empty(m, 0, 0)
        self.assertEqual(check, True, "The right weight of the matrix is not checking if container is empty correctly")
    
    def test_bc(self):
        bc = balance_calc(10, 10)
        self.assertEqual(bc, 0, "The balance calculation is not correct")

    def test_con2bc(self):
        s = State(0, 10, 10, True)
        check = con2_balance_check(s, 20, 10)
        self.assertEqual(check, True, "The balance condition 2 is not satisfied")

class TestBoundChecks(unittest.TestCase):
    def testIsEmpty(self):
        testFile = "ShipCase4.txt"
        listOfContainers = FileRead(testFile)
        m = matrix(listOfContainers, 8, 12)
        empty = isEmpty(m, m[1][1], m[1][2])
        self.assertEqual(empty, True, "IsEmpty fails to selects a valid empty space")

    def testIsEmptyFails(self):
        testFile = "ShipCase4.txt"
        listOfContainers = FileRead(testFile)
        m = matrix(listOfContainers, 8, 12)
        empty = isEmpty(m, m[1][1], m[2][1])
        self.assertEqual(empty, False, "IsEmpty fails to selects a valid empty space")
    
    def testPathToContainer(self):
        testFile = "ShipCase5.txt"
        listOfContainers = FileRead(testFile)
        m = matrix(listOfContainers, 8, 12)
        actionList, new_matrix = pathToNewContainer(m, m[0][4], m[0][6])
        self.asseertEqual(actionList, True, )
if __name__ == "__main__":
    unittest.main()