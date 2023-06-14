from sample_time import rejectSampling, funcSampling, truncSampling

if __name__ == '__name__':
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
  print('over')
