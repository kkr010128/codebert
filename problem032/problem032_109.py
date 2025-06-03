n=int(input())
s_str=[]
for i in range(2):
    s_str.append(input().split())
s_int=[]
for i in s_str:
    s_int.append([int(s) for s in i])
manh=0
yu=0
p_3=0
che=[]
for i in range(n):
    manh+=abs(s_int[0][i]-s_int[1][i])
    yu+=(s_int[0][i]-s_int[1][i])**2
    p_3+=(abs(s_int[0][i]-s_int[1][i]))**3
    che.append(abs(s_int[0][i]-s_int[1][i]))
print(manh)
print(yu**(1/2))
print(p_3**(1/3))
print(max(che))
