import numpy as np
from scipy.stats import norm,truncnorm
from functools import reduce
import time

def rejectSampling(message,length,mesbit_len):
    z = np.zeros(length)
    fenmu = float(2**mesbit_len)

    for i in range(length):
        dec_mes = reduce(lambda a,b: 2*a+b, message[mesbit_len*i:mesbit_len*(i+1)])
        dec_mes = float(dec_mes)
        while 1:
            z[i] = np.random.standard_normal()
            if z[i]>norm.ppf(dec_mes/fenmu) and z[i]<=norm.ppf((dec_mes+1)/fenmu):
                break 
    return z
def funcSampling(message,length,mesbit_len):
    z = np.zeros(length)
    fenmu = float(2**mesbit_len)
    for i in range(length):
        dec_mes = reduce(lambda a,b: 2*a+b, message[mesbit_len*i:mesbit_len*(i+1)])
        dec_mes = float(dec_mes)
        u = np.random.rand()
        z[i] = norm.ppf((u+dec_mes)/(2**mesbit_len))
    return z
def truncSampling(message,length,mesbit_len):
    z = np.zeros(length)
    fenmu = float(2**mesbit_len)
    ppf=[]
    for j in range(int(fenmu)+1):
        ppf.append(norm.ppf(j/fenmu))
    for i in range(length):
        dec_mes = reduce(lambda a,b: 2*a+b, message[mesbit_len*i:mesbit_len*(i+1)])
        dec_mes = int(dec_mes)
        z[i] = truncnorm.rvs(ppf[dec_mes],ppf[dec_mes+1])
    return z
length = 1000
reject_time = []
fun_time = []
trunc_time = []
z1 = []
z2 = []
z3 = []
for mesbit_len in range(1,9):
    message = np.random.rand(length*mesbit_len)
    t1 = time.time()
    z1_ = rejectSampling(message,length,mesbit_len)
    t2 = time.time()
    z1.append(z1_.mean())
    reject_time.append(t2-t1)
    t1 = time.time()
    z2_ = funcSampling(message,length,mesbit_len)
    t2 = time.time()
    z2.append(z2_.mean())
    fun_time.append(t2-t1)
    t1 = time.time()
    z3_ = truncSampling(message,length,mesbit_len)
    t2 = time.time()
    z3.append(z3_.mean())
    trunc_time.append(t2-t1)
print(reject_time,fun_time,trunc_time,sep='\n')
print(np.mean(z1),np.mean(z2),np.mean(z3))
