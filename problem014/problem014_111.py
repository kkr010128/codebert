NN=raw_input()
N=raw_input()
A = [int(i) for i in N.split()]
swap=0

for i in range(int(NN)):
  for j in reversed(range(i+1,int(NN))):
    if A[j] < A[j-1] :
      t = A[j]
      A[j] = A[j-1]
      A[j-1] = t
      swap+=1
      
print ' '.join([str(k) for k in A])
print swap