s = input()

a = [0] * (len(s)+1)

larger_count = 0
for i in range(len(s)):
    if s[i] == '>':
        larger_count += 1
        continue
    
    for j in range(larger_count+1):
        a[i-j] = max(a[i-j], j)
    larger_count = 0
    a[i+1] = a[i] + 1

for j in range(larger_count+1):
    a[len(a)-j-1] = max(a[len(a)-j-1], j)

print(sum(a))