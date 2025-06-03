n = int(input())
*a, = map(int, input().split())
print(sum(i%2 for i in a[::2]))