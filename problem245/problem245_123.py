N = int(input())
S = str(input())
count = 0
for n in range(N-1):
    if S[n:n+3] == "ABC":
        count += 1
print(count)