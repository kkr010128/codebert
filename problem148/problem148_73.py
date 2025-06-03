A,B,C,K = map(int,input().split())
SCO = 0
if A>K:
    SCO+=K
else:
    SCO+=A
    if B<=(K-A):
        if C<=(K-A-B):
            SCO-=C
        else:
            SCO-=K-A-B
print(SCO)