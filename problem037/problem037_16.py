S = int(input())
s = S % 60
m1 = S // 60
m = m1 % 60
h = m1 // 60
print(str(h)+':'+str(m)+':'+str(s))