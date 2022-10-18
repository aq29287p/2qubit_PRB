# 2qubit_PRB
We execute randomized benchmarking in 2 qubit channel.  
main file :  
execute rb and fit and polt  
preparation file :  
generate gateset data and Clifford data  

#===========================================  

rb_seq:  
gate number is 1 to 100  
a=[1,2,3,4,5,6, 8, 10, 13, 16, 20, 25, 32, 40, 50, 63, 79, 100, 126, 158, 200, 251, 316, 398, 501, 631, 794, 1000, 1,259, 1,585, 1,995, 2,512, 3,162]  
repeat number is 1000  
2-qubit depolarizing:  
p to do nothing  
1-p to totally mixed state (I, X, Y, Z)^2  
2-qubit dephasing  
p to do nothing  
1-p to totally dephasing (I, Z)^2  
#===========================================  
RB : rb_seq.pkl => gateset  
IRB : irb_seq.pkl =>  
#----  
PRB : rb_2_prb_seq  ====> from rb seq   
IPRB : iprb_seq ====> random choose  
