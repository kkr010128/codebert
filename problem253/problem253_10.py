N,A,B = list(map(int,input().split()))
if (B-A)%2 == 0:
    print((B-A)//2)
    exit()
A1 = A
B1 = B
A2 = A
B2 = B
count1 = N-B1
ans1 = 0
A1 += (N-B1)
B1 = N
if (B1-A1)%2 == 0:
    ans1 = count1+(B1-A1)//2
else:
    ans1 = count1+1+(B1-A1)//2

count2 = A2-1
ans2 = 0
B2 -= (A2-1)
A2 = 1
if (B2-A2)%2 == 0:
    ans2 = count2+(B2-A2)//2
else:
    ans2 = count2+1+(B2-A2)//2
print(min(ans1,ans2))