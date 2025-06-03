n = int(input())
a,b = input().split()
print(''.join(a[i]+b[i] for i in range(n)))