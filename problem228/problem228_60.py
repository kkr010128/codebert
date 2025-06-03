H = int(input())
cnt = 0
while(H>1):
    H //= 2
    cnt += 1

if H == 1:
    print(2**(cnt+1)-1)

else:
    print(2**cnt-1)