n,k=map(int,input().split())
lst_ans=[]
for i in range(k):
  s=int(input())
  lst_n=list(map(int,input().split()))
  for j in lst_n:
    lst_ans.append(j)
print(n-len(set(lst_ans)))