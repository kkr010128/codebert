inp = input().split(" ")
count = 0
for x in range(int(inp[0]),int(inp[1])+1):
    if x % int(inp[2]) == 0:
        count = count+1
print(count)

