n = int(input())

count = 0
ans = 0
for i in range(n):
    s = input().split()
    
    if s[0]==s[1]:
        count += 1
    else:
        count = 0
        
    if count ==3:
        print('Yes')
        exit(0)

else:
    print('No')