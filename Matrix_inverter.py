class Matrix_inverter(object):#Gauss-Jordan method 3x3
    in_matrix = [[0,0,0],[0,0,0],[0,0,0]]
    res_matrix = [ [1, 0, 0], [0, 1, 0], [0 , 0 , 1] ]

    def __init__(self):
        self.in_matrix = [[0,0,0],[0,0,0],[0,0,0]]
        self.res_matrix = [ [1, 0, 0], [0, 1, 0], [0 , 0 , 1] ]

        #for i in range (0, 3):
         #   for j in range (0, 3):
          #      self.in_matrix[i][j] = matrix[i][j]


    def invert(self, matrix):
        self.in_matrix = matrix
        #forvard_elimination
        for pivot in range(0, 2): # "2' means n-1
            if abs(self.in_matrix[pivot][pivot]) > 0.001:
                for m in range (pivot+1, 3): # from 1 to n
                    coef = self.in_matrix[m][pivot] / self.in_matrix[pivot][pivot]
                    self.res_matrix[m][pivot] -= self.res_matrix[pivot][pivot] * coef
                    for j in range (0,3):
                        self.in_matrix[m][j] -= coef * self.in_matrix[pivot][j]
        for pivot in range(2, 0, -1):
            if abs(self.in_matrix[pivot][pivot]) > 0.001:
                for m in range (pivot - 1, -1, -1): # from 1 to n
                    coef = self.in_matrix[m][pivot] / self.in_matrix[pivot][pivot]
                    for j in range (0,3):
                        self.res_matrix[m][j] -= self.res_matrix[pivot][j] * coef
                        self.in_matrix[m][j] -= coef * self.in_matrix[pivot][j]
        return self.res_matrix

