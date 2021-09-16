import timeit

def f1():
	for n in range(100):
		pass

def f2():
	n = 0
	while n < 100:
		n += 1

import numpy as np
def matrix_mul(MatA, MatB):
    assert MatA.shape[1] == MatB.shape[0], 'The dimensions do not match'
    print(MatA.shape[0],MatB.shape[1] )
    MatC = np.zeros((MatA.shape[0], MatB.shape[1]))
    for i in range(0,MatA.shape[0]):
        for j in range(0,MatB.shape[1]):
            for k in range(0,MatA.shape[1]):
                MatC[i,j] += MatA[i,k] * MatB[k, j]
    return MatC

def test_matrix_mul():
	len_ = 100
	MatA = np.random.rand(len_, len_)
	MatB = np.random.rand(len_, len_)
	matrix_mul(MatA, MatB)
#


#print(timeit.timeit(f1, number= 10000))
print(timeit.timeit(f2, number= 10000))
#print(timeit.timeit(test_matrix_mul, number= 2))
