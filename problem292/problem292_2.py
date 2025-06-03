N = int(input())
D = list(map(int,input().split()))
print((sum(D)**2-sum(list(map(lambda x:x**2,D))))//2)