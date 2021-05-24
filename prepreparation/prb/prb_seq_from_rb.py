from functools import reduce
import pickle
with open('rb_seq_gateset1.pkl', 'rb') as f:
    rb = pickle.load(f)
b=sorted(reduce(lambda x,y: x+y, [i for i in list(rb.values())]),key=len)
c={}
d=b[0]
for i in b[1:]:
    if len(i)==len(b[b.index(i)-1]):
        d.append(i)
    else:
        c[len(b[b.index(i)-1])]=d
        d=[]
        d.append(i)
with open('rb_2_prb_gateset1.pkl', 'wb') as f:
    pickle.dump(c,f)   
