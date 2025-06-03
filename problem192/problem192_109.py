n = int(input())
A = list(map(int, input().split()))
freq = [0] * (max(A)+1)
for a in A:
    freq[a] += 1
total = 0
for f in freq:
    total += f*(f-1)//2
for a in A:
    print (total - max(freq[a]-1, 0))