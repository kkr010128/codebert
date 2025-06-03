d = int(input())
c = list(map(int,input().split()))
s = [0]*d
for i in range(d):
    s[i] = list(map(int,input().split()))
lis = [0]*26
sum_score = 0
for i in range(d): #d日全てに対して
    ans = -float("Inf")
    num = 0
    for j in range(26): #i日目にj番目を選んだ時の得点を計算
        score = 0
        score += s[i][j]
        for k in range(26):
            if k != j:
                score -= (lis[k]+1)*c[k]
        if score > ans:
            ans = score
            num = j
    sum_score += ans
    #print(sum_score)
    print(num+1)
    for j in range(26):
        if j != num:
            lis[j] += 1
        else:
            lis[j] = 0
    #print(lis)