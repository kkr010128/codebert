from scipy.sparse import*
_,*s=open(0)
*g,=eval('[0]*500,'*500)
i=-1
for t in s:
 i+=1;j=0
 for u in t:k=i*20+j;g[k][k+1]=u>'#'<t[j+1];g[k][k+20]=u>'#'<(s+['#'*20])[i+1][j];j+=1
a=csgraph.johnson(csr_matrix(g),0)
print(int(max(a[a<999])))