n = int(input())
s = input()
lis = list(s)

ans = s.count("R") * s.count("B") * s.count("G")

for i in range(n):
    if lis[i] == "R":
        lis[i] = 1
    elif lis[i] == "G":
        lis[i] = 2
    else:
        lis[i] = 4

for i in range(n):
    for j in range(i+1, n):
        k = 2*j -i
        if k >= n:
            continue
        if lis[i] + lis[j] + lis[k] == 7:
            ans -= 1
        
print(ans)