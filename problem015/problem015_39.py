NN=raw_input()
N=raw_input()
A = [int(i) for i in N.split()]
swap=0

for i in range(int(NN)):
  mini = i
  for j in range(i,int(NN)):
    if A[j] < A[mini]:
      mini = j
  if i != mini:
    t = A[i]
    A[i] = A[mini]
    A[mini] = t
    swap+=1
      
print ' '.join([str(k) for k in A])
print swap