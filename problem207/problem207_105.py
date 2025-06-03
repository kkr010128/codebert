A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))

A = list()
A.append("")
A.extend(A1)
A.extend(A2)
A.extend(A3)

n = int(input())
B = list()
for _ in range(n):
    B.append(int(input()))

holes = [A.index(b) for b in B if (b in A)]
bingos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
print("Yes" if any([(len(set(holes) & set(bingo)) == 3) for bingo in bingos]) else "No")