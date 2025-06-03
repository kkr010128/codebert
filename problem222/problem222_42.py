N = int(input())
A = list(map(int, input().split()))

dic = {}

for i in A:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1
    
print("YES" if max(dic.values()) == 1 else "NO")