from  Matrix_inverter import Matrix_inverter
from LU_Factorizator import LU_Factorizator


class Equasion_solver(object):#Gauss-Jordan method 3x3
    in_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    in_vector = [0,0,0]



    def matr_mult(self, L_matrix, U_matrix):
        rez_matr = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range (0,3):
            for j in range (0,3):
                for k in range (0,3):
                    rez_matr[i][j] += U_matrix[k][j] * L_matrix[i][k]
        return rez_matr


    def LU_solve(self, matrix, vector):
        lu_factorizator = LU_Factorizator()
        L_matr, U_matr = lu_factorizator.factorize(matrix)
        #print (L_matr)
        #print (U_matr)
        #print (self.matr_mult(L_matr, U_matr))
        semi_res = self.A_inv_solve(L_matr, vector)
        #print (semi_res)
        res = self.A_inv_solve(U_matr, semi_res)
        #print (res)
        return res


    def __init__(self):
        self.in_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.in_vector = [0, 0, 0]

    def matr_vector_mult(self, matrix, vector):
        rez_vector = [0,0,0]
        for i in range (0,3):
            for j in range (0,3):
                rez_vector[i] += matrix[i][j] * vector[j]
        return rez_vector

    def A_inv_solve(self, matrix, vector):
        rez_vector = []
        matrix_inverter = Matrix_inverter()
        inverted_matrix = matrix_inverter.invert(matrix)
        rez_vector = self.matr_vector_mult(inverted_matrix, vector)
        return rez_vector

"""
test_matrix = [[1,0,1],[0,1,1],[1,0,2]]
test_vector = [1,0,1]
solver = Equasion_solver()

rez_vector = solver.LU_solve(test_matrix, test_vector)
print (rez_vector)
"""