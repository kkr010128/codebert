A,B,C,K = map(int,input().split())

score = 0

if A<K:
    K -= A
    score += A
else:
    score += K
    print(score)
    exit()

if B<K:
    K -= B
else:
    print(score)
    exit()

score -= min(K,C)
print(score)