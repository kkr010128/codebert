def choose_hand(last,next):
    for j in ['r','s','p']:
        if j!=last and j!=next:
            return j

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
        lastHand = rpsList[i-k]
        nextHand = hands[t[i+k]] if i+k<n  else ''
        rpsList[i] = choose_hand(lastHand,nextHand)
    else:
        ans += points[hands[hand]]

print(ans)