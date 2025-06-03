N,K = map(int,input().split())
list1 ={i for i in range(1,N+1)}
list2 = set()
for i in range(K):
  NN = int(input())
  MM = map(int,input().split())
  for j in MM:
    list2.add(j)

ans = list1 -list2
print(len(ans))