ans = 0
def do(x,c,index):
    global ans
    # print "c : " + str(c)
    # print "x : " + str(x)
    # print "index : "+ str(index)
    # print "###############"
    if index < 0:
        return
    if x < 0:
        return
    if c>=3 and x!=0:
        return
    if x == 0 and c!=3:
        return
    if c==3 and x==0:
        # print "detect!"
        ans += 1
        return
    for i in reversed(xrange(1,index+1)):
        # print "i : "+ str(i)
        do(x-i,c+1,i-1)
    return

while True:
    n,x = map(int,raw_input().split())
    if n==0 and x == 0:
        break
    # nlist = [i for i in xrange(1,n+1)]
    # print nlist
    do(x,0,n)
    # print "ans : "+str(ans)
    print ans
    ans = 0