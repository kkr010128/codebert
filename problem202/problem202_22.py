# import math
# import statistics
# a=input()
#b,c=int(input()),int(input())
# c=[]
# for i in a:
#     c.append(i)
e1,e2,e3 = map(int,input().split())
# f = list(map(int,input().split()))
#g = [input() for _ in range(a)]
# h = []
# for i in range(e1):
#     h.append(list(map(int,input().split())))

ba1=e1//(e2+e3)
ba2=e1-ba1*(e2+e3)
if ba2<=e2:
    print(ba2+ba1*e2)
elif ba2>e2:
    print(e2+ba1*e2)