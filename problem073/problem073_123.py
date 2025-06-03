N=int(input())
count=0
#N未満の値がaで割り切れさえすればいい
for a in range(1,N):
    count = count + (N-1)//a
print(count)