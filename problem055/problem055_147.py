import sys
def reviewRe():
    #print ' '.join(map(str,map(str,residence[i][j])))
    for area in range(4):
        for floor in range(3):
            sys.stdout.write(' ')
            print ' '.join(map(str,residence[area][floor][:]))
        if area <= 2:
            print "####################"

def move_in():
    n=input()
    for i in range(n):
        b,f,r,v = map(int,raw_input().split())
        adding(b,f,r,v)

def adding(b,f,r,v):
    residence[b-1][f-1][r-1] += v


if __name__ == '__main__':
    residence = [[[0 for room in range(10)] for floor in range(3)] for area in range(4)]
    move_in()
    reviewRe()