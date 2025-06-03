d = input().split()
dicry = {'N':'152304', 'E':'310542', 'W':'215043','S':'402351'}
for i in input():
    d = [d[int(c)] for c in dicry[i]]
    
print(d[0])
