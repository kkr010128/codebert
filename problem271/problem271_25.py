N=int(input())
S=input()
tmp=""
for i in range(len(S)):
  chtmp=ord(S[i])+N
  if(chtmp>ord('Z')):
    chtmp-=(ord('Z') - ord('A') + 1)
  tmp+=chr(chtmp)
print(tmp)
