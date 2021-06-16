#create primitive_kraus
import pickle
from pyquil.simulation.matrices import I, X, Y, CNOT
import numpy as np
from forest.benchmarking.operator_tools import kraus2pauli_liouville
from print_large import _print_big_matrix
from scipy.linalg import block_diag
def swap(M):
    SWAP = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    return np.dot(np.dot(SWAP, M), SWAP)
#primitive gates
X_2 = 0.5* np.asarray([[1+1j,   1-1j], [1-1j,  1+1j]])
Y_2 =  np.asarray([[1+0.j,   -1], [1,  1]])/np.sqrt(2)

###HPCNOT
'''P = np.asarray([[1, 0], [0, 1j]])
H_P_CNOT_kruas=[
    np.kron(I, H),
    np.kron(H, I),
    np.kron(I, P),
    np.kron(P, I),
    block_diag(I,X),
    block_diag(X,I)]'''
###gateset1
'''
P_kruas = [ np.kron(I, I),
np.kron(X_2, I),
np.kron(I, X_2),
np.kron(X, I),
np.kron(I, X),
np.kron(-X_2, I),
np.kron(I,-X_2),
np.kron(Y_2, I),
np.kron(I, Y_2),
np.kron(Y, I),
np.kron(I, Y),
np.kron(-Y_2, I),
np.kron(I, -Y_2),
CNOT,
swap(CNOT)]
'''

#gate set 2
P_kruas = [  
np.kron(X_2, I),
np.kron(I, X_2),
np.kron(Y_2, I),
np.kron(I, Y_2),
CNOT,
swap(CNOT)]



##############################
P_PTM=[kraus2pauli_liouville(i) for i in P_kruas]

with open('P_kruas_gateset2.pkl', 'wb') as f:
    pickle.dump(P_kruas, f)
with open('P_PTM_gateset2.pkl', 'wb') as f:
    pickle.dump(P_PTM, f)