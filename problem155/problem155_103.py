N,M = map(int,input().split())
a_list = list(map(int,input().split()))
list_n = [0]*(N+1)
for i in range(M):
  
  a,b = map(int,input().split())
  a_n = a_list[a-1]
  b_n = a_list[b-1]
  if a_n == b_n:
    list_n[a]-=10000
    list_n[b]-=10000
  elif a_n>b_n:
    list_n[a] +=1
    list_n[b] -= 10000
  elif a_n<b_n:
    list_n[b] +=1
    list_n[a] -= 10000
count =0
for i in range(1,N+1):
  if list_n[i]>=0:
    count+=1
print(count)