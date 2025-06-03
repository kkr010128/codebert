b = input()
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
max_a = max(a)
min_a = min(a)
Sum = sum(a)
print(min_a,max_a,Sum)
