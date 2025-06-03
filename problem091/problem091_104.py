N = int(input())
L = list(map(int,input().split()))
if N < 3:
    print(0)
    exit()
count = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        if L[i] == L[j]:
            continue
        else:
            for k in range(j+1,N):
                if L[i]==L[k] or L[j]==L[k]:
                    continue
                elif abs(L[i]+L[j])>L[k]and abs(L[i]-L[j])<L[k]:
                    count += 1
print(count)