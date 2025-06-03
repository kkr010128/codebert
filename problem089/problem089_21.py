import queue
h,w,m = ( int(x) for x in input().split() )

h_array = [ 0 for i in range(h) ]
w_array = [ 0 for i in range(w) ]
ps = set()
for i in range(m):
    hi,wi = ( int(x)-1 for x in input().split() )
    h_array[hi] += 1
    w_array[wi] += 1
    ps.add( (hi,wi) )
h_great = max(h_array)
w_great = max(w_array)
h_greats = list()
w_greats = list()
for i in range( h ):
    if h_array[i] == h_great:
        h_greats.append(i)
for i in range( w ):
    if w_array[i] == w_great:
        w_greats.append(i)

ans = h_great + w_great - 1

escaper = False

for i in range( len(h_greats) ):
    hi = h_greats[i]
    for j in range( len(w_greats) ):
        wi = w_greats[j]
        if (hi,wi) not in ps:
            ans += 1
            escaper = True
            break
    if escaper:
        break

print(ans)