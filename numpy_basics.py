import numpy as np

matrix_a = np.array([[i for i in range(1,4)],[i for i in range(4,7)],[i for i in range(7,10)]])
print(matrix_a)

matrix_b = np.array([[i for i in range(9,6,-1)],[i for i in range(6,3,-1)],[i for i in range(3,0,-1)]])
print(matrix_b)

product = matrix_a * matrix_b

print(product)