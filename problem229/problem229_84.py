import sys

def main(args):
    h, n = map(int,input().split())
    
    magic = [0]*n
    maxim = 0
    for i in range(n):
        dam, mp = map(int,input().split())
        magic[i] = (dam, mp)
        maxim = max(maxim, dam)
    
    damage = [float('inf')]*(2*10**4)
    damage[0] = 0
    for i in range(max(2*h, 2*maxim)):
        for m in magic:
            dam, mp = m
            damage[i] = min(damage[i-dam]+mp, damage[i])
    
    print(min(damage[h:]))

if __name__ == '__main__':
    main(sys.argv[1:])