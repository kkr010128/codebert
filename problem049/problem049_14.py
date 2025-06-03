H=[]
W=[]
while 1:
    h,w=map(int,raw_input().split())
    if h==w==0:
        break
    H.append(h)
    W.append("#"*w)
for i in xrange(len(W)):
    for j in xrange(H[i]):
        print(W[i])
    print