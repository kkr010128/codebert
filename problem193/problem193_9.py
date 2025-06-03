H,W,K = map(int,input().split())
A = []
for i in range(H):
    b = list(input())
    b.append("0")
    A.append(b)

ans = 10**6
for i in range(2**(H-1)):
    p = "0" + str(H-1)
    bin_list = list(format(i,p+"b"))
    sec = []
    for i in range(H-1):
        if bin_list[i] == "1":
            sec.append(i)
    sec.append(H-1)
    l = len(sec)

    W_start = 0
    k = 0
    while(True):
        H_start = 0
        pross = 10**4
        for i in range(l):
            H_end = sec[i] + 1
            j = W_start
            c = 0
            while(True):
                for t in range(H_start,H_end):
                    if A[t][j] == "1":
                        c += 1
                j += 1
                if c > K or j > W:
                    pross = min(pross,j-W_start)
                    break
            H_start = sec[i] + 1

        k += 1
        W_start += pross-1
        if W_start > W-1 or pross == 1:
            break
    if pross != 1:
        ans = min(ans,k+l-2)

print(ans)