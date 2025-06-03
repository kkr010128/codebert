nn, kk = list(map(int,input().split()))

sum = 0
for i in range(kk, nn+2):
    min = (0+i-1)*i/2
    max = (nn+nn-i+1)*i/2
    sum += (max-min)+1

sum = sum % (10**9+7)
print(int(sum))