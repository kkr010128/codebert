N=int(input())
c=str(input())
num_R = c.count("R")
num_W = 0
ans = []
if num_R >= num_W:
    ans.append(num_R)
else:
    ans.append(num_W)
#print(ans)
for i in range(len(c)):
    if c[i] == "R":
        num_R -= 1
    else:
        num_W += 1
    if num_R >= num_W:
        ans.append(num_R)
    else:
        ans.append(num_W)
    #print(ans)
print(min(ans))
