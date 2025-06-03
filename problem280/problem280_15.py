import itertools
import math
#print(3 & (1 << 0))
def main():
    N = int(input())
    items = [i+1 for i in range(N)]

    locations=[]
    for i in range(N):
        locations.append(list(map(int, input().split())))

    paths =list(itertools.permutations(items))

    sum = 0
    for path in paths: # path = [1,2,3,4,5]
        for i in range(len(path)-1):
            from_idx = path[i] -1
            to_idx = path[i+1] -1
            xdiff= locations[from_idx][0] - locations[to_idx][0]
            ydiff= locations[from_idx][1] - locations[to_idx][1]
            sum = sum + math.sqrt(xdiff**2 + ydiff**2)
    print( sum / len(paths))
main()
