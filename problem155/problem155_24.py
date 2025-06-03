n, m = map(int, input().split())
h = list(map(int, input().split()))
 
roads = []
for i in range(n): roads.append([])
 
is_good_peak_arr = [True] * n
for i in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    if h[a] >= h[b]: is_good_peak_arr[b] = False
    if h[b] >= h[a]: is_good_peak_arr[a] = False
 
print(is_good_peak_arr.count(True))