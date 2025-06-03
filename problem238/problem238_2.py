n, k, s = map(int, input().split())

for i in range(n):
    if k == 0:
        if s-1 > 0:
            print(s-1, end=' ')
        else:
            print(s+1, end=' ')
    else:
        print(s, end=' ')
        k -= 1
print()
        
