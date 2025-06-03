numsA = [int(e) for e in input().split()]
numsB = [int(e) for e in input().split()]
T = int(input())
if abs(numsA[0]-numsB[0])<=(numsA[1]-numsB[1])*T:
    print("YES")
else:
    print("NO")
