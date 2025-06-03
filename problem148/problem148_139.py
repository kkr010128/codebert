import sys
A,B,C,K=map(int, sys.stdin.readline().split())
ans=0
a_cards=min(K,A)
K-=a_cards
ans+=a_cards*1

b_cards=min(K,B)
K-=b_cards
ans+=b_cards*0

c_cards=min(K,C)
K-=c_cards
ans+=c_cards*-1

print ans
