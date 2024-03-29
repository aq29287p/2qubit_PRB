#find inverse
import pickle
import numpy as np
from print_large import _print_big_matrix
from tqdm import tqdm
from multiprocessing import Process, Pool


with open('Cliff_kruas.pkl', 'rb') as f:
    Cliff_kruas = pickle.load(f)

def fun(j):
    for k in range(len(Cliff_kruas)-1):
        l=np.conj(Cliff_kruas[j]@Cliff_kruas[i]).T
        if np.isclose(np.absolute(np.trace(l@Cliff_kruas[k])), 4):
            Cliff_inverse_index[(i%1152)*11520+j]=k
            break

        else:
            assert k != (len(Cliff_kruas)-1), "no inverse"
    return None

if __name__ == '__main__':
    Cliff_inverse_index = np.zeros(1152*11520)
    label=int(input('0~9'))*1152
    for i in tqdm(range(label,label+1152), desc="outter"):
        pool = Pool()
        pool.map(fun,[j for j in range(len(Cliff_kruas)-1)])
        pool.close()
        pool.join()
        with open('Cliff_inverse_index'+str(label/1152)+'.pkl', 'wb') as f:
            pickle.dump(Cliff_inverse_index, f)  
            #results = [int(_i) for _i in filter(None, results)]
            #assert len(results)==1, 'not one inverse'
            #Cliff_inverse_index += results

            

  
