n = input()
data = map(int, raw_input().split())
newdata = sorted(data)
sum = 0
for i in range(n):
    #print newdata[i]
    sum += newdata[i]

print "%d %d %d" %(newdata[0], newdata[n-1], sum)