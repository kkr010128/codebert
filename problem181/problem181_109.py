K=int(input())
ans=[]
def saiki(A):
    genzai_saigo=int(A[-1])
    ketasu=len(A)
    if ketasu>0:
        B="".join(A)
        ans.append(eval(B))
    if ketasu==10:
        return
    for i in [genzai_saigo-1,genzai_saigo,genzai_saigo+1]:
        if i < 0 or i>9:
            continue
        A.append(str(i))
        saiki(A)
        A.pop()
for i in range(1,10):
    saiki([str(i)])
ans.sort()
print(ans[K-1])