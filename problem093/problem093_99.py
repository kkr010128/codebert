n, k =map(int, input().split())
p = list(map(int, input().split()))
c = list(map(int, input().split()))
roop = []
seen = [0 for  _ in range(n)]
count = 0
for i in range(n):
    if seen[i]>0:
        continue
    else:
        count+=1
        seen[i] = count
        roop.append([c[i]])
        t = i
        while i!=p[t]-1:
            seen[p[t]-1]=count
            roop[-1].append(c[p[t]-1])
            t = p[t]-1
#print(seen)
#print(roop)
ans = max(c)

for i in roop:
    #print(ans)
    
    s = sum(i)
    ii = i+i
    #print(ii)
    if len(i)>=k:
        for j in range(1, k+1):
            temp = sum(ii[:j])
            for l in range(len(i)):
                if l!=0:
                    temp+=ii[l+j-1]
                    temp-=ii[l-1]
                    #temp = sum(ii[l:l+j])
                #print(i, j, l, temp)
                ans  = max(ans, temp)
    else:
        for j in range(1, len(i)+1):
            temp=  sum(ii[:j])
            for l in range(len(i)):
                if l != 0:
                    temp+=ii[l+j-1]
                    temp-=ii[l-1]
                #print(temp)
                if s>0:
                    temp1 = temp+s*((k-j)//len(i))
                else:
                    temp1 = temp
                
                #print(i, j, l, temp)
                ans  = max(ans, temp)
                ans  = max(ans, temp1)
            
print(ans)

        
