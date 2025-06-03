n = int(input())
s = input()
R = s.count("R")
G = s.count("G")
B = s.count("B")

total = R*G*B

for i in range(n-1):
    for j in range(i+1,n):
        if j*2-i < n:
            if s[i] != s[j] and s[j] != s[j*2-i] and s[i] != s[j*2-i]:
                total -= 1
        else:
            continue

print(total)