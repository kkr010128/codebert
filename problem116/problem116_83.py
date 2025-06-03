a = list(input())
b = list(input())
num = len(a)
S = 0

for i in range(num):
    if a[i] != b[i]:
        S += 1
        
print(S)