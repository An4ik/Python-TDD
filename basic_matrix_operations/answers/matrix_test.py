from unittest import TestCase
import matrix as m
class MatrixOperations(TestCase):

    def test_get_mat_add(self):
        a=[[1, 2, 3], [4, 5, 6], [8, 9, 0]]
        b=[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        c=[[2, 3, 4], [6, 7, 8], [11, 12, 3]]
        result=m.mat_add(a,b)
        self.assertEqual(result,c)

    def test_get_mat_sub(self):
        a=[[1, 2, 3], [4, 5, 6], [8, 9, 0]]
        b=[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        c=[[0, 1, 2], [2, 3, 4], [5, 6, -3]]
        result=m.mat_sub(a,b)
        self.assertEqual(result,c)

    def test_get_transpose(self):
        a=[[1, 2, 3], [4, 5, 6], [8, 9, 0]]
        b=[[1, 4, 8], [2, 5, 9], [3, 6, 0]]
        result=m.mat_transpose(a)
        self.assertEqual(result,b)

    def test_check_matrix(self):
        a=[[1, 2, 3], [4, 5, 6], [8, 9, 0]]
        b=[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        result=m.mat_check(a,b)
        self.assertTrue(result)

    def test_check_multip(self):
        a=[[1, 2, 3], [4, 5, 6], [8, 9, 0]]
        b=[[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        result=m.mat_check_multip(a,b)
        self.assertTrue(result)
    def test_get_mat_multip(self):
        a=[[1, 1, 1], [0, 0, 0], [3, 3, 3]]
        b=[[1, 1, 1], [0, 0, 0], [3, 3, 3]]
        c=[[4, 4, 4], [0, 0, 0], [12, 12, 12]]
        result=m.mat_multip(a,b)
        self.assertEqual(result,c)
    def test_get_mat_div(self):
        matrix1=[[1,2,3],[3,2,1],[2,1,3]]
        matrix2=[[4,5,6],[6,5,4],[4,6,5]]
        c=[[0,0,0],[0,0,0],[0,0,0]]
        result=m.mat_division(matrix1, matrix2)
        self.assertEqual(result, c)
