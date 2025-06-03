#a=int(input())
#b,c=int(input()),int(input())
# c=[]
#  for i in b:
#     c.append(i)
H,N = map(int,input().split())
f = list(map(int,input().split()))
#j = [input() for _ in range(a)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))
if sum(f)>=H:
    print("Yes")
else:
    print("No")