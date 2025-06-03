N=int(input())
cnt=0
for i in range(int(N/2)):
    if (i+1)!=(N-i-1):
      cnt+=1
print(cnt)
