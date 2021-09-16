import time
import numpy as np

# O(a n^3 + b n^2 + c n + d)
def matrix_mul(MatA, MatB):
    assert MatA.shape[1] == MatB.shape[0], 'The dimensions do not match'
    print(MatA.shape[0],MatB.shape[1] )
    MatC = np.zeros((MatA.shape[0], MatB.shape[1]))
    for i in range(0,MatA.shape[0]):
        for j in range(0,MatB.shape[1]):
            for k in range(0,MatA.shape[1]):
                MatC[i,j] += MatA[i,k] * MatB[k, j]
    return MatC

def build_in_matrxi_mul(MatA, MatB):
    return np.matmul(MatA, MatB)

len_list = []
time_list = []


for i in range(1, 21):
    len_ = i * 5
    MatA = np.random.rand(len_, len_)
    MatB = np.random.rand(len_, len_)
    start = time.time()
    matrix_mul(MatA, MatB)
    #build_in_matrxi_mul(MatA, MatB)
    end = time.time()
    len_list.append(len_)
    time_list.append(end - start)

import matplotlib.pyplot as plt
plt.plot(len_list, time_list,'o')
plt.show()

