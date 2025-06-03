def print_residence(residence):
    for i in range(4):
        for j in range(3):
            print " " +" ".join(map(str, residence[i][j]))
        if i != 3:
            print "####################"

n = int(raw_input())
residence = [[[0] * 10 for i in range(3)] for j in range(4)]
#print_residence(residence)

for i in range(n):
    info = map(int, raw_input().split())
    #print info
    #print residence
    residence[info[0]-1][info[1]-1][info[2]-1] += info[3] 
    #print residence

print_residence(residence)