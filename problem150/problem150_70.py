N, K = map(int, input().split())
A = list(map(lambda x:int(x)-1, input().split()))

cnts = [None] * N

pos = 0
cnt = 0

while cnt < K:
    if cnts[pos] != None:
        loop_size = cnt - cnts[pos]
        cnt += ((K-cnt-1) // loop_size) * loop_size
        cnts = [None] * N
    cnts[pos] = cnt
    pos = A[pos]
    cnt += 1

print(pos+1)

