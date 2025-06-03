n,m = map(int,input().split())
Ai = list(map(int,input().split()))
list.sort(Ai, reverse=True)
print('Yes' if Ai[m-1]>= sum(Ai) / (4 * m) else 'No')