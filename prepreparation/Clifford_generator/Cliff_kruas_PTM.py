#create Cliff_kraus and PTM
import pickle
import numpy as np
with open('Cliff_indices_(HPCNOT).pkl', 'rb') as f:
    Prim = pickle.load(f)
from tqdm import trange
#primitive gates
global H
global P
global CNOT
global I
H = (1/np.sqrt(2))*np.array([[1, 1], [1, -1]])
P = np.array([[1, 0], [0, 1j]])
CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
I = np.identity(2)

def swap(M):
    SWAP = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    return np.dot(np.dot(SWAP, M), SWAP)

def get_gate(primkey):    
    if primkey == 0:
        return np.kron(I, H)
    elif primkey == 1:
        return swap(np.kron(I, H))
    elif primkey == 2:
        return np.kron(I, P)
    elif primkey == 3:
        return swap(np.kron(I, P))
    elif primkey == 4:
        return CNOT
    elif primkey == 5:
        return swap(CNOT)
    else:
        return np.identity(4)
    
def get_unitary(keylist):
    M = np.identity(4)
    for i in range(len(keylist)):
        M = get_gate(keylist[i]) @ M
    return M
Cliff_kraus=[]       
Cliff_PTM=[]  
for i in trange(len(Prim)):
    A = get_unitary(Prim[i])
    Cliff_kraus.append(A)
    from forest.benchmarking.operator_tools import kraus2pauli_liouville
    Cliff_PTM.append(kraus2pauli_liouville(A))
with open('Cliff_kruas.pkl', 'wb') as f:
    pickle.dump(tuple(Cliff_kraus), f)
with open('Cliff_PTM.pkl', 'wb') as f:
    pickle.dump(tuple(Cliff_PTM), f)

