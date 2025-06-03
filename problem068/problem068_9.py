def convert():
    str = input().rstrip()
    n = int(input().rstrip())
    
    for _ in range(n):
        columns = input().rstrip().split()
        order = columns[0]
        a = int(columns[1])
        b = int(columns[2])
        
        if order == 'print':
            print(str[a:b+1])
            
        if order == 'reverse':
            str = str[:a] + str[a:b+1][::-1] + str[b+1:]
        
        if order == 'replace':        
            p = columns[3]
            str = str[:a] + p + str[b+1:] 
if __name__ == '__main__':
    convert()
