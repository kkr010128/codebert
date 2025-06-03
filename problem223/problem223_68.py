n,k = map(int, input().split()) 

p = [int(x) for x in input().split()]
p_kitaiti=[float((x+1)/2) for x in p]

ruisekiwa=[p_kitaiti[0]]

for i in range(1,len(p_kitaiti)):
    ruisekiwa.append(ruisekiwa[-1]+p_kitaiti[i])

ans=ruisekiwa[k-1]

for i in range(1,len(ruisekiwa)-k+1):
    ans=max(ans,ruisekiwa[i+k-1]-ruisekiwa[i-1])

print(ans)