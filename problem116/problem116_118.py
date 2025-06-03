S=raw_input()
T=raw_input()
ans=0
for s,t in zip(S,T):
    if s!=t:
        ans+=1
print ans