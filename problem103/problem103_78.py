N = int(input(""))
a = input("").split(" ")
a = [int(i) for i in a]
m = 1000
list_ = []

for j in range(0, N-1):
    if a[j] < a[j + 1]:
        n = m // a[j]
        k = (a[j + 1] - a[j]) * n
        m = m + k

print(m)