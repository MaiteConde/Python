import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la

a = np.array([1,2,3,4,5], dtype='i')
b = np.array([1,6,3,4,9], dtype='f')
print(a)
print(b)
c = np.array([[1,2,3], [4,5,6]])
print(c[0,2])

C = np.array ([[[5,6,7], [2,8,9]],[[-5,-6,-7], [-2,-8,-9]]])


#Position
print(C[1,0,2])

#Number of array dimensions
print(C.ndim)

# lengths of the corresponding array dimensions.
print(C.shape)

#Total bytes consumed by the elements of the array.
print(C.nbytes)

#Return evenly spaced values within a given interval. [start, final, interval]
A = np.arange(20,100,3)
print(A)

#Randomly permute a sequence, or return a permuted range.
B = np.random.permutation(A)
print(B)


Random values in a given shape.
D = np.random.rand(100)
#Two dimensional array
F = np.random.rand(2,3)
print(plt.hist(D))

#Return a sample (or samples) from the “standard normal” distribution.
E = np.random.randn(100)
print(E)


Gives a new shape to an array without changing its data.
G = np.arange(100).reshape(4,25)
print(G)

#Slice
H = np.arange(100)

print(H[3:19])
print(H[::-3])

I = np.round(10*np.random.rand(5,4))
I.sort(axis=1)
print(I[1,2])
print(I[1,:])
print(I[:,1])
print(I[1:3, 2:4])


J = np.arange(50)
K = J[[3,5,7]]
print(K)


L = np.round(10*np.random.rand(2,3))
M = np.round(10*np.random.rand(2,3))
print(M)
print(L)
print(L + 3)
print(L + (np.arange(2).reshape(2,1)))
N = np.hstack((L,M))
print(N)




