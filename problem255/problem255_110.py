n=int(input())
s,t = map(str, input().split())
print(''.join([s[i] + t[i] for i in range(0,n)]))