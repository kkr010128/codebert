k=int(input())

ans=0
import itertools
import math
for seq in itertools.combinations_with_replacement(range(1,k+1),3):
    if seq[0]==seq[1] or seq[1]==seq[2]:
        if  seq[0]!=seq[2]:
            ans+=(math.gcd(seq[0],math.gcd(seq[1],seq[2])))*3
        else:
            ans+=math.gcd(seq[0],math.gcd(seq[1],seq[2]))

    else:
        ans+=math.gcd(seq[0],math.gcd(seq[1],seq[2]))*6
print(ans)