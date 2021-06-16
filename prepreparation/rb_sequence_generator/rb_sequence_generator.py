#rb seq w/ inverse
from functools import reduce
import numpy as np
import pickle
from print_large import _print_big_matrix
from tqdm import trange
from multiprocessing import  Pool
### 2-qubit Clifford matrix
with open('Cliff_kruas.pkl', 'rb') as f:
    Cliff_kruas = pickle.load(f)
###generate rb sequence
def rb_seq_fun(seq_number):
    np.random.seed()
### random choose 11520 Clifford matrix
    rb_seq_index= np.random.randint(low=0, high=11520, size=seq_number).tolist()
### rb sequence matrix
    rb_seq_kraus=reduce(lambda x, y : y@x, [Cliff_kruas[_i] for _i in rb_seq_index])
### find rb inverse element
    for i_rb in range(11520):
        if (np.isclose(abs(np.trace(Cliff_kruas[i_rb]@rb_seq_kraus)),4)):
            rb_seq_index.append(i_rb)
            return rb_seq_index
        elif i_rb == 11519:
            return False
if __name__ == '__main__':
    rb_seq={}
    max_seq_number=int(input('max sequence number'))
    types=int(input('different types sequence '))
    for i in trange(1,max_seq_number):
        pool=Pool()
        rb_seq[i]=pool.map(rb_seq_fun,[i]*types)
        assert False not in rb_seq[i], 'false in rbseq'
        pool.close()
        pool.join()
    with open('rb_seq.pkl', 'wb') as f:
        pickle.dump(rb_seq, f)
        