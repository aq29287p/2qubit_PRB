#prb seq w/inverse
import random
from functools import reduce
import numpy as np
import pickle
from print_large import _print_big_matrix
from tqdm import trange
from multiprocessing import Pool
#### 2-qubit pauli basis
with open('H_P_CNOT_kruas.pkl', 'rb') as f:
    Primitive_kruas = pickle.load(f)
#### weighted
Primitive_weights=[15694, 12780, 20232, 15752, 12124, 10492]

def prb_seq_fun(seq_number):
    random.seed()
    prb_seq_index= random.choices([_i for _i in range(len(Primitive_kruas))], weights=Primitive_weights, k=seq_number)
    prb_seq_kraus=reduce(lambda x, y : y@x, [Primitive_kruas[_i] for _i in prb_seq_index])

    for i_rb in range(len(Primitive_kruas)):
        if (np.isclose(abs(np.trace(Primitive_kruas[i_rb]@prb_seq_kraus)),4)):
            prb_seq_index.append(i_rb)
            return prb_seq_index
        elif i_rb==len(Primitive_kruas):
            return None
if __name__ == '__main__':
    prb_seq={}
    max_seq_number=int(input('max sequence number'))
    types=int(input('different types sequence '))
    for i in trange(1,max_seq_number):
########init_        
        prb_seq[i]=[0]
#        while(len(prb_seq[i])<types and j<100):
        pool=Pool()
        _prb_seq=pool.map(prb_seq_fun,[i]*types*100)
        prb_seq[i]=list(filter(None,_prb_seq))
        pool.close()
        pool.join()

'''    with open('prb_seq.pkl', 'wb') as f:
        pickle.dump(prb_seq, f)'''