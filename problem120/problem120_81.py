NN = input().split()
N = int(NN[0])
K = int(NN[1])
LL = input().split()
list1 =[]
for i in LL:
  list1.append(int(i))
list1.sort()

total = 0
for i in range(K):
  total += list1[i]
print(total)