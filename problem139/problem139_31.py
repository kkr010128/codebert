h1, m1, h2, m2, k = list(map(int, input().split()))
#n, m = list(map(int, input().split()))
# a = list(map(int, input().split()))
# data = [list(map(int, input().split())) for i in range(n)]
# k = int(input())
# a = list(map(int, input().split()))
# ab_sorted = sorted(ab, key=lambda x: x[0])
#py = [list(map(int, input().split())) for i in range(m)]
# b = list(map(int, input().split()))


total = (h2-h1)*60
if m1 <= m2:
    total += (m2-m1)
else:
    if m2 == 0:
        total += 60-m1
        total -= 60
    else:
        #total += (m1-m2)
        total -= (m1-m2)


ans = total - k
print(ans)
