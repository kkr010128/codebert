
while True:
    
    line = input()
    
    if line=='-':
        break
    
    loop = int(input())
    
    for i in range(loop):
        x = int(input())
        line = line[x:] + line[:x]
    print(line)



