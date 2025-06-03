# ABC155E

s = input()
d0 = [0,1,2,3,4,5,6,7,8,9]
d1 = [0,1,2,3,4,5,5,4,3,2] # 通常時

a0 = d1[int(s[0])]
a1 = d1[int(s[0]) + 1] if int(s[0])<=8 else 1

for c in s[1:]:
    c = int(c)
    b0 = min(a0 + c, a1 + (10 - c))
    b1 = min(a0 + c + 1, a1 + (9 - c)) if c <=8 else a1
    a0, a1 = b0, b1
    
print(a0)