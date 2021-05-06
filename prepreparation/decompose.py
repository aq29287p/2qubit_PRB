import numpy as np
# import copy
import itertools
import pickle



def swap(M):
    SWAP = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    return np.dot(np.dot(SWAP, M), SWAP)

'''
Functions "Gates_multi" and "Is_New" act on the following matrix object:
M = [ [decompose series], [matrix form] ]
"Decompose series" is in the form [generator1, qn], [generator2, qn]......
'''
#Matrix multiplication
def Gates_multi(M1, M2):
    a = M1[0] + M2[0]
    b = np.dot(M1[1], M2[1])
    return [a, b]

#Determine whether a matrix M is new to a set M_array.
def Is_New(M_array, M):
    for n in range(len(M_array)):
        if np.allclose(np.absolute(np.trace(np.dot(M_array[n][1].conj().T, M[1]))), 4):
            # print(M_array[n][0], "\n", M[0], "\n\n")
            return False
        else:
            continue
    return True


I = np.identity(2)
X = np.asarray([[0,   1], [1,  0]])
Y = np.asarray([[0, -1j], [1j, 0]])
Z = np.asarray([[1,   0], [0, -1]])
X_2 = 0.5* np.asarray([[1+1j,   1-1j], [1-1j,  1+1j]])
Y_2 =  np.asarray([[1+0.j,   -1], [1,  1]])/np.sqrt(2)
#primitive gates
H = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]])
P = np.array([[1, 0], [0, 1j]])
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])

#generate all possible primitive gates set
Prim = [ [[0], np.kron(I, I)],
         [[1], np.kron(X_2, I)],
         [[2], np.kron(I, X_2)],
         [[3], np.kron(X, I)],
         [[4], np.kron(I, X)],
         [[5], np.kron(-X_2, I)],
         [[6], np.kron(I,-X_2)],
         [[7], np.kron(Y_2, I)],
         [[8], np.kron(I, Y_2)],
         [[9], np.kron(Y, I)],
         [[10], np.kron(I, Y)],
         [[11], np.kron(-Y_2, I)],
         [[12], np.kron(I, -Y_2)],
         [[13], CNOT],
         [[14], swap(CNOT)] ]
'''
gate set 2
Prim = [ [[0], np.kron(X_2, I)],
         [[1], np.kron(I, X_2)],
         [[2], np.kron(Y_2, I)],
         [[3], np.kron(I, Y_2)],
         [[4], CNOT],
         [[5], swap(CNOT)] ]
'''

'''
Computational searching all possible clifford elements.
'''

Cliff_2 = []
Cliff_index = []
L = []
c = 0
count = 0
#Iterate first Zv's
for i in range(len(Prim)):
    a = Prim[i]
    if Is_New(Cliff_2, a):
        Cliff_2.append(a)
        Cliff_index.append(a[0])
        c += 1
        count += 1
#         print(count)
    else:
        continue
L.append(c)
c = 0

t = 1
d = 0
while True:
    if t > 1:
        d += L[t-2]
    for i in range(d, len(Cliff_2)):
        for j in range(len(Prim)):
            a = Gates_multi(Prim[j], Cliff_2[i])
            if Is_New(Cliff_2, a):
                Cliff_2.append(a)
                Cliff_index.append(a[0])
                c += 1
                count += 1
                if count % 10 == 0:
                    print(count)
            if len(Cliff_2) == 11520:
                break
            else:
                continue
        if len(Cliff_2) == 11520:
            break
        else:
            continue
    L.append(c)
    c = 0
    t += 1
    if len(Cliff_2) == 11520:
        break
    else:
        continue

with open('Cliff_index_gateset1.pkl', 'wb') as f:
    pickle.dump(Cliff_index, f)

print(L, "\n")
# print(Cliff_2[199][0], "\n\n", Cliff_2[199][1])
# print(Cliff_index)