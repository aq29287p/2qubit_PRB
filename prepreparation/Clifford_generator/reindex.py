import pickle
import multiprocessing as mp
from tqdm import trange
import numpy as np
from collections import Counter
###gateset
gateset=int(input('gateset 1,2,3'))
with open('Cliff_matrix_gateset'+str(gateset)+'.pkl', 'rb') as f:
    C_g = pickle.load(f)
with open('Cliff_kruas.pkl', 'rb') as f:
    C = pickle.load(f)
with open('Cliff_index_gateset'+str(gateset)+'.pkl', 'rb') as f:
    c_index = pickle.load(f)
def fun(_j):
    if np.isclose(abs(np.trace(C_g[i][1]@C[_j].conj().T))/4,1):
        return [i,_j]
if __name__ == '__main__':
    a=[]
    for i in trange(11520):
        pool = mp.Pool()
        res=pool.map_async(fun,[_j for _j in range(11520)]).get()

        pool.close()
        pool.join()

        a.append([i for i in filter(lambda x: x!=None, res)][0])

    b = dict(Counter(np.asarray(a).T[1]))
    print ({key:value for key,value in b.items()if value > 1})
    new_C=[False]*11520
    new_c_inedx=[False]*11520
    for i in a:
        new_C[i[1]]=C_g[i[0]][1]
        c_index[i[0]].reverse()
        new_c_inedx[i[1]]=c_index[i[0]]

    with open('Cliff_matrix_gateset'+str(gateset)+'_reindex.pkl', 'wb') as f:
        pickle.dump(new_C, f)
    with open('Cliff_index_gateset'+str(gateset)+'_reindex.pkl', 'wb') as f:
        pickle.dump(new_c_inedx, f)
