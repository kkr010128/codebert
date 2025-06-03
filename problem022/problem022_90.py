n = input()
S = raw_input().split()
q = input()
T = raw_input().split()

s = 0
for i in T:
    if i in S:
        s+=1
print s