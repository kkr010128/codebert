h = int(input())
cnt = 0
while h > 1:
    h //= 2
    cnt += 1
print(2**(cnt+1)-1)