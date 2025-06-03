str_1=input()
q=int(input())
for _ in range(q):
   lst=list(input().split())
   res = (lst[0])
   a = int(lst[1])
   b = int(lst[2])+1
  
   if res=='print':
     print(str_1[a:b])
   elif res=='replace':
    str_1=str_1[:a]+lst[3]+str_1[b:]
   elif res=='reverse':
    str_1=str_1[:a] + str_1[a:b][::-1] + str_1[b:]