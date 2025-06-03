n,k = map(int,input().split())
r,s,p = map(int,input().split())
points = {'r':r, 's':s, 'p':p}
hands = {'r':'p', 's':'r', 'p':'s'}
t = list(input())
rpsList = ['']*n
ans = 0

for i,hand in enumerate(t):
    rpsList[i] += hands[hand]
    if i>=k and rpsList[i]==rpsList[i-k]:
        last_hand= rpsList[i-k]
        next_hand = hands[t[i+k]] if i+k<n else ''
        for j in ['r','s','p']:
            if j!=last_hand and j!=next_hand:
                rpsList[i] = j
    else:
        ans += points[hands[hand]]

print(ans)