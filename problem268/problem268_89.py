N = int(input())
A = list(map(int,input().split()))
# print(A)
RGB = [1,0,0]
M = 1000000007

c = 3

f = False
if A[0] != 0:
    f = True

for i in range(1,N):
    try:
        cnt = RGB.count(A[i])
        idx = RGB.index(A[i])
    except:
        f = True
        break
    c = (c * cnt)%M
    RGB[idx] += 1
    # print(RGB)
if f:
    print(0)
else:
    print(c)