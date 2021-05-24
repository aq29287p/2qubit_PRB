#transform rb sequence into prb sequence 
import pickle
import itertools
gateset=int(input('gateset 1,2'))
with open('rb_seq.pkl', 'rb') as f:
    rb_seq = pickle.load(f)
with open('Cliff_index_gateset'+str(gateset)+'_reindex.pkl', 'rb') as f:
    decomp = pickle.load(f)

c={}
f={}
for i in rb_seq:
    b=[]
    for j in rb_seq[i]:
        a=[]
        for k in j:
            a.append(decomp[k])
        e=list(itertools.chain.from_iterable(a))
        b.append(e)
    c[i]=b
with open('rb_seq_gateset'+str(gateset)+'.pkl', 'wb') as f:
    pickle.dump(c, f)
