S = input()
T = input()
ans = 0

for i,y in zip(S,T):
    if i != y:
       ans += 1 

print(ans)