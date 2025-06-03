n = int(input())
s = input()

freq = {'R': 0, 'G': 0, 'B': 0}
for x in s:
    freq[x] += 1

ans = freq['R'] * freq['G'] * freq['B']
for i in range(n-2):
    for j in range(i+1, n-1):
        k = j + (j-i)
        if k < n and s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
            ans -= 1

print(ans)
