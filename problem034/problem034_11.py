rot_set = [
    (1,2,4,3,1), #0
    (0,3,5,2,0), #1
    (0,1,5,4,0), #2
    (0,4,5,1,0), #3
    (0,2,5,3,0), #4
    (1,3,4,2,1)  #5
]

dice_int = list(map(int, input().split()))
q = int(input())
right_face = []

for _ in range(q):
    a, b = map(int, input().split())
    a_idx = dice_int.index(a)
    b_idx = dice_int.index(b)

    for i in range(6):
        for j in range(4):
            if (a_idx, b_idx) == (rot_set[i][j], rot_set[i][j+1]):
                right_face.append(dice_int[i])

for i in range(q):
    print(right_face[i])
