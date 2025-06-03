def imas(hoge_l, p, track):
    s_weights = 0
    now_track = 1
    for val in hoge_l:
        s_weights += val
        if s_weights > p:
            s_weights = val
            now_track += 1
        if now_track > track:
            return False
    return True

num, track = [int(x) for x in input().split()]
hoge_l = list()
for _ in range(num):
    hoge_l.append(int(input()))
left = 0
right = 100000 * 10000

while left < right :
    mid = (right + left) // 2
    if imas(hoge_l, mid, track):
        right = mid 
    else:
        left = mid + 1
        
max_num = max(hoge_l)
if max_num > right:
    right = max_num
print (right)
