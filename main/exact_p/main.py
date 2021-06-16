#rb seq and find inverse
import random
import numpy as np
import pickle
from print_large import _print_big_matrix
from tqdm import tqdm
from multiprocessing import Process, Pool
#### 2-qubit pauli basis
with open('Cliff_kruas.pkl', 'rb') as f:
    Cliff_kruas = pickle.load(f)
def rb_seq_fun(seq_number):
    np.random.seed()
    rb_seq_index= np.random.randint(low=0, high=11520, size=seq_number).tolist()
    rb_seq_kraus=np.eye(4)
    for i_rb in rb_seq_index:
        rb_seq_kraus=Cliff_kruas[i_rb]@rb_seq_kraus
    for i_rb in range(11520):
        c=np.conj(rb_seq_kraus).T
        d=Cliff_kruas[i_rb]
        a=abs(np.trace(c@d))
        if (np.isclose(a,4)):
            rb_seq_index.append(i_rb)
            break
        else:
            #assert i_rb != 11519, 'no inverse'
            continue
    return rb_seq_index
if __name__ == '__main__':
    rb_seq={}
    #Max=int(input('max sequence number'))
    #types=int(input('different types sequence '))
    Max=5
    types=1
    for i in range(1,Max):

        pool=Pool()
        _rb_seq=pool.map(rb_seq_fun,[i]*types)
        rb_seq[i]=_rb_seq
        pool.close()
        pool.join()