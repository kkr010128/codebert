s = [input() for i in range(2)]
count=0
for item1, item2 in zip(s[0], s[1]):
    if (item1 != item2):
        count +=1
        
print(count)