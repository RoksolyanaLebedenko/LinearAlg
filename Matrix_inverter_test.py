class Matrix_inverter(object):#Gauss-Jordan method 3x3
    in_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    res_matrix = [ [1, 0, 0], [0, 1, 0], [0 , 0 , 1] ]

    def __init__(self, matrix):
        self.in_matrix = matrix
        for i in range (0, 3):
            for j in range (0, 3):
                self.in_matrix[i][j] = matrix[i][j]


    def invert(self):
        #forvard_elimination
        for pivot in range(0, 2): # "2' means n-1
            if abs(self.in_matrix[pivot][pivot]) > 0.001:
                for m in range (pivot+1, 3): # from 1 to n
                    coef = self.in_matrix[m][pivot] / self.in_matrix[pivot][pivot]
                    self.res_matrix[m][pivot] -= self.res_matrix[pivot][pivot] * coef
                    for j in range (0,3):
                        self.in_matrix[m][j] -= coef * self.in_matrix[pivot][j]
        print(self.in_matrix[0])
        print(self.in_matrix[1])
        print(self.in_matrix[2])
        print(self.res_matrix[0])
        print(self.res_matrix[1])
        print(self.res_matrix[2])
        for pivot in range(2, 0, -1):
            if abs(self.in_matrix[pivot][pivot]) > 0.001:
                for m in range (pivot - 1, -1, -1): # from 1 to n
                    coef = self.in_matrix[m][pivot] / self.in_matrix[pivot][pivot]
                    for j in range (0,3):
                        self.res_matrix[m][j] -= self.res_matrix[pivot][j] * coef
                        self.in_matrix[m][j] -= coef * self.in_matrix[pivot][j]


        #reverse_elimination
        print("______________")
        print(self.in_matrix[0])
        print(self.in_matrix[1])
        print(self.in_matrix[2])
        print("______________")

        print(self.res_matrix[0])
        print(self.res_matrix[1])
        print(self.res_matrix[2])
        return self.res_matrix


"""
        coef0_1 = self.in_matrix [1][0] / self.in_matrix [0][0]
        self.res_matrix [1][0] -=  coef0_1 * self.res_matrix[0][0]
        for j in range (0, 3):
            self.in_matrix[1][j] = self.in_matrix[1][j] - coef0_1 * self.in_matrix[0][j]
        coef0_2 = self.in_matrix [2][0] / self.in_matrix [0][0]
        print(self.res_matrix[0])
        print(self.res_matrix[1])
        print(self.res_matrix[2])
        for j in range (0, 3):
            self.in_matrix[2][j] = self.in_matrix[2][j] - coef0_2 * self.in_matrix[0][j]
        self.res_matrix [2][0] -=  coef0_2 * self.res_matrix[0][0]
        print(self.res_matrix[0])
        print(self.res_matrix[1])
        print(self.res_matrix[2])
        if abs(self.in_matrix[1][1]) > 0.0001:
            coef1_2 = self.in_matrix[2][1] / self.in_matrix[1][1]
            for j in range(1, 3):
                self.in_matrix[2][j] = self.in_matrix[2][j] - coef1_2 * self.in_matrix[0][j]
            self.res_matrix [2][1] -=  coef1_2 * self.res_matrix[1][1]
        print(self.res_matrix[0])
        print(self.res_matrix[1])
        print(self.res_matrix[2])
"""        """
        if abs(self.in_matrix[1][2]) > 0.0001:
            coef2_1 = self.in_matrix[1][2] / self.in_matrix[2][2]
            for j in range(1, 3):
                self.in_matrix[2][j] = self.in_matrix[2][j] - coef2_1 * self.in_matrix[0][j]
            self.res_matrix [2][1] -=  coef2_1 * self.res_matrix[1][1]
            coef2_0 = self.in_matrix[0][2] / self.in_matrix[2][2]
            for j in range(1, 3):
                self.in_matrix[2][j] = self.in_matrix[2][j] - coef2_0 * self.in_matrix[0][j]
            self.res_matrix[2][1] -= coef2_1 * self.res_matrix[1][1]
        print(self.res_matrix[0])
        print(self.res_matrix[1])
        print(self.res_matrix[2])
        """

test_matr = [[1,0,1], [0,1,1],[1,0,2]]
m_inv = Matrix_inverter(test_matr)
rez = m_inv.invert()
print (rez)
print(m_inv.in_matrix)