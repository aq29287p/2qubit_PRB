###### i prb seq  ### random select from p
from functools import reduce
from itertools import permutations, chain
import numpy as np
import pickle
import os
from print_large import _print_big_matrix
from tqdm import tqdm
from multiprocessing import Pool
a=[1,2,3,4,5,6, 8, 10, 13, 16, 20, 25, 32, 40, 50, 63, 79, 100, 126, 158, 200, 251, 316, 398, 501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162]
def irb_seq(_iprb_seq):
    total_operation=reduce(lambda x,y: y@x, [P[_i] for _i in _iprb_seq])
### find irb inverse element
    for _i in range(len(P)):
        if (np.isclose(abs(np.trace(P[_i]@total_operation)),4)):
            _iprb_seq.append(_i)
            return _iprb_seq
        
if __name__ == '__main__':
    gateset=int(input('gateset \n'))
    interleaved_gate_index=int(input('interleaved gate number \n'))
    rep=int(input('repeat \n'))
    gateset_path=str(os.path.abspath(os.path.join(os.getcwd(), "../..")))+'/gateset/'
    if gateset==1:
        gate_distri=[1, 9601, 8129, 3103, 2296, 0, 0, 9285, 8118, 2974, 3058, 0, 0, 10523, 9788]
    elif gateset==2:
        gate_distri=[16192, 11846, 15055, 13880, 10476, 10481]
    with open(gateset_path+'gateset'+str(gateset)+'/P_kruas_gateset'+str(gateset)+'.pkl', 'rb') as f:
        P = pickle.load(f)
    with open(gateset_path+'gateset'+str(gateset)+'/Cliff_index_gateset'+str(gateset)+'_reindex.pkl', 'rb') as f:
        C_gateset = pickle.load(f)



    iprb_seq={}
    for i in tqdm(a):

###random choice#######################################################################################################
######## all possible combination        
        if i<6:
            seq= [list(_i) for _i in list(permutations([_j for _j in range(len(P))], r=i))]
######## random choices            
        else:
            np.random.seed()
            seq=np.random.choice([_i for _i in range(len(P))],size=(rep,i),p=[_i / sum(gate_distri) for _i in gate_distri]).tolist()
###flatten list
        flattenlist = lambda nestedlist:[item for element in nestedlist for item in flattenlist(element)] if type(nestedlist) is list else [nestedlist]
###interleaved gate in P
        seq=[flattenlist(list(chain(*[lst[_i:_i+1] + [C_gateset[interleaved_gate_index]] if len(lst[_i:_i+1]) == 1 else lst[_i:_i+1] for _i in range(len(lst))]))) for lst in seq]

###cal the inverse        
        pool=Pool()
#### filter None
        iprb_seq[i]=list(filter(None, pool.map_async(irb_seq,seq).get()))
        pool.close()
        pool.join()
##### end for loop #################################################################################################
    with open(str(interleaved_gate_index)+'iprb_seq_gateset'+str(gateset)+'.pkl', 'wb') as f:
        pickle.dump(iprb_seq, f)