a = input()
ar = [0 for i in range(len(a)+1)]
for i in range(len(a)):
    if a[i] == '<':
        ar[i+1] = max(ar[i] + 1,ar[i+1])
for i in range(len(a)-1,-1,-1):
    if a[i] == '>':
        ar[i] = max(ar[i+1] + 1,ar[i])
print(sum(ar))