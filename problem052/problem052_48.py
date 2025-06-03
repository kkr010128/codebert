import sys

def call(n):
    i = 1
    while i <= n:
        x = i
        if x % 3 == 0:
            print(' ', i, sep='', end='')
        else:
            while x:
                if x % 10 == 3:
                    print(' ', i, sep='', end='')
                    break

                x //= 10
            
        i += 1
        
    print('')
    
if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    call(n)