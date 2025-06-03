import sys
def I(): return int(sys.stdin.readline().rstrip())

def Main():
    x = I()
    for a in range(-118,120):
        for b in range(-118,120):
            if a**5-b**5 == x:
                print(a,b)
                exit()
    return

if __name__=='__main__':
    Main()