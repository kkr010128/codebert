import bisect

n, m, k = list(map(int, input().split()))
book_a = list(map(int, input().split()))
book_b = list(map(int, input().split()))

a_time_sum = [0]
b_time_sum = []
for i in range(n):
    if i == 0:
        a_time_sum.append(book_a[0])
    else:
        a_time_sum.append(a_time_sum[i]+book_a[i])

for i in range(m):
    if i == 0:
        b_time_sum.append(book_b[0])
    else:
        b_time_sum.append(b_time_sum[i-1]+book_b[i])

ans = 0

# Aから何冊か読む
for i in range(n+1):
    read = i
    a_time = a_time_sum[i]
    time_remain = k - a_time
    if time_remain < 0:
        break
    # このときBから何冊よめる？
    b_read = bisect.bisect_right(b_time_sum, time_remain)
    read += b_read
    ans = max(ans, read)

print(ans)
