H = [[[0 for x in xrange(10)] for j in xrange(3)] for i in xrange(4)]
n = input()

for x in range(n):
        b,f,r,v = map(int, raw_input().split())
        H[b-1][f-1][r-1] += v

for b in range(4):
        for f in range(3):
                print(' '+' '.join(map(str,H[b][f])))
        if b != 3:
                print ('#'*20)