s,t = map(int,input().split())
print('Yes' if s*2 <= t <= s*4 and t%2 == 0 else 'No')