N=int(input())
s_str=input().split()
s_int=[int(s) for s in s_str]
list=[]
s_int.reverse()
for i in s_int:
    list.append(i)
print(" ".join(map(str, list)))


