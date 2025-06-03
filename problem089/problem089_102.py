import sys
input = sys.stdin.readline

h,w,m = map(int,input().split())

h_array = [ 0 for i in range(h) ]
w_array = [ 0 for i in range(w) ]
ps = set()
for i in range(m):
    hi,wi = map( lambda x : int(x) - 1 , input().split() )
    h_array[hi] += 1
    w_array[wi] += 1
    ps.add( (hi,wi) )

h_great = max(h_array)
w_great = max(w_array)
h_greats = list()
w_greats = list()
for i , hi in enumerate(h_array):
    if hi == h_great:
        h_greats.append(i)
for i , wi in enumerate(w_array):
    if wi == w_great:
        w_greats.append(i)

ans = h_great + w_great


for _h in h_greats:
    for _w in w_greats:
        if (_h,_w) in ps:
            continue
        print(ans)
        exit()

print(ans-1)