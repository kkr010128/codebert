N = [int(i) for i in input()]
n = N[::-1]+[0]
for i in range(len(n)-1):
    if n[i] >= 6 or (n[i] == 5 and n[i+1] >= 5):
        n[i] = 10 - n[i]
        n[i+1] += 1
print(sum(n))
