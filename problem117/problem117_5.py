import bisect


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_books = 0

sum_a = []
sum_b = []

total = 0
for i in range(n):
    total += a[i]
    sum_a.append(total)

total = 0
for j in range(m):
    total += b[j]
    sum_b.append(total)

sum_a.insert(0, 0)
sum_b.insert(0, 0)

for i in range(n+1):
    r = k - sum_a[i]
    if r == 0:
        books = i
    elif r < 0:
        books = 0
    else:
        book_b = bisect.bisect_right(sum_b, r)
        books = i + book_b - 1
    if books >= max_books:
        max_books = books

print(max_books)

