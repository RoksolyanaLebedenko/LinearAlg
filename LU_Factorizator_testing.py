class LU_Factorizator(object):#Gauss-Jordan method 3x3
    U_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    L_matrix = [ [1, 0, 0], [0, 1, 0], [0 , 0 , 1] ]

    def __init__(self, matrix):
        self.U_matrix = matrix
        for i in range (0, 3):
            for j in range (0, 3):
                self.U_matrix[i][j] = matrix[i][j]


    def factorize(self):
        #forvard_elimination
        for pivot in range(0, 2): # "2' means n-1
            if abs(self.U_matrix[pivot][pivot]) > 0.001:
                for m in range (pivot+1, 3): # from 1 to n
                    coef = self.U_matrix[m][pivot] / self.U_matrix[pivot][pivot]
                    self.L_matrix[m][pivot] += self.L_matrix[pivot][pivot] * coef
                    for j in range (0,3):
                        self.U_matrix[m][j] -= coef * self.U_matrix[pivot][j]
        print(self.U_matrix[0])
        print(self.U_matrix[1])
        print(self.U_matrix[2])
        print("_______________")
        print(self.L_matrix[0])
        print(self.L_matrix[1])
        print(self.L_matrix[2])
        print (self.matr_mult())
        return self.U_matrix


    def matr_mult(self):
        rez_matr = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range (0,3):
            for j in range (0,3):
                for k in range (0,3):
                    rez_matr[i][j] += self.U_matrix[k][j] * self.L_matrix[i][k]
        return rez_matr


        #print(self.res_matrix[0])
        #print(self.res_matrix[1])
        #print(self.res_matrix[2])
        """
        for pivot in range(2, 0, -1):
            if abs(self.in_matrix[pivot][pivot]) > 0.001:
                for m in range (pivot - 1, -1, -1): # from 1 to n
                    coef = self.in_matrix[m][pivot] / self.in_matrix[pivot][pivot]
                    for j in range (0,3):
                        self.res_matrix[m][j] -= self.res_matrix[pivot][j] * coef
                        self.in_matrix[m][j] -= coef * self.in_matrix[pivot][j]
"""

test_matr = [[1,0,1], [0,1,1],[1,0,2]]
m_LU = LU_Factorizator(test_matr)
rez = m_LU.factorize()
print (rez)
#print(m_inv.in_matrix)