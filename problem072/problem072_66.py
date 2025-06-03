s=int(input())
d = [list(map(int,input().split())) for _ in range(s)]

def p(val):
    print(val)

def calc(s,d):
    for i in range(s-2):
        if d[i][0] == d[i][1] and d[i+1][0]==d[i+1][1] and d[i+2][0] == d[i+2][1]:
            
            return 'Yes'
    
    return 'No'

        
p(calc(s,d))