a,b = input().split()

a = int(a)
b_list = list(b)
b_list.pop(1)
b_list = [int(s) for s in b_list]

p_100 = a*b_list[0]*100 + a*b_list[1]*10 + a*b_list[2]
p = p_100//100

print(p)