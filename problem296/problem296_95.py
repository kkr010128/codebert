S = list(input())
K = int(input())
 
ans = 0
#２つ並べて一般性を確かめる
S2 = S*2

for i in range(1,len(S2)):
    if S2[i-1]== S2[i]:
        S2[i] = '@'
        #2回目以降はk-1回任意の@へ直す
        if i>=len(S2)//2:
            ans+= K-1
        else:
            ans+=1
            
if len(set(S)) ==1 and len(S)%2 !=0:
   ans = len(S)*(K//2)+(K%2==1)*(len(S)//2)
print(ans) 