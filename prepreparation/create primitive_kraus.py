#create primitive_kraus
import pickle
from pyquil.simulation.matrices import I, X, Y, Z ,H, CNOT
import numpy as np
from forest.benchmarking.operator_tools import kraus2pauli_liouville
from print_large import _print_big_matrix
from scipy.linalg import block_diag

P = np.asarray([[1, 0], [0, 1j]])
H_P_CNOT_kruas=[
    np.kron(I, H),
    np.kron(H, I),
    np.kron(I, P),
    np.kron(P, I),
    block_diag(I,X),
    block_diag(X,I)]
    
H_P_CNOT_PTM=[kraus2pauli_liouville(i) for i in H_P_CNOT_kruas]

with open('H_P_CNOT_kruas.pkl', 'wb') as f:
    pickle.dump(H_P_CNOT_kruas, f)
with open('H_P_CNOT_PTM.pkl', 'wb') as f:
    pickle.dump(H_P_CNOT_PTM, f)