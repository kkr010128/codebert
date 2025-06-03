#
# 179A
#
s = input()
s1 = list(s)

if s1[len(s)-1]=='s':
    print(s+'es')
else:
    print(s+'s')