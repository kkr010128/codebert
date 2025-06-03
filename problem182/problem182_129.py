n, k, c = map(int, input().split())
s = list(input())
left = []
right = []

i = 0
while i < n:
    if len(left) >= k:
        break
    if s[i] == "o":
        left.append(i)
        i += c + 1
    else:
        i += 1
i = n - 1
while i >= 0:
    if len(right) >= k:
        break
    if s[i] == "o":
        right.append(i)
        i -= c + 1
    else:
        i -= 1

for i in range(k):
    if left[i] == right[k - 1 - i]:
        print(left[i] + 1)