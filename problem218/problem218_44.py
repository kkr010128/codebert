N=int(input())
kouholist=[]
worddict=dict()
maxvalue=0
for i in range(N):
    S=input()
    if S in worddict.keys():
        worddict[S]+=1
    else:
        worddict[S]=1
    maxvalue=max(maxvalue,worddict[S])
#print("ここから")
#print(worddict)
for k in worddict.keys():
    if worddict[k]==maxvalue:
        kouholist.append(k)
kouholist=sorted(kouholist)
for h in range(len(kouholist)):
    print(kouholist[h])