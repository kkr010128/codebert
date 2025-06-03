d = {
    (1,2): 3,
    (1,3): 5,
    (1,4): 2,
    (1,5): 4,
    (2,1): 4,
    (2,3): 1,
    (2,4): 6,
    (2,6): 3,
    (3,1): 2,
    (3,2): 6,
    (3,5): 1,
    (3,6): 5,
    (4,1): 5,
    (4,2): 1,
    (4,5): 6,
    (4,6): 2,
    (5,1): 3,
    (5,3): 6,
    (5,4): 1,
    (5,6): 4,
    (6,2): 4,
    (6,3): 2,
    (6,4): 5,
    (6,5): 3
}

v = list(map(int, input().split()))
q = int(input())
questions = []
for _ in range(q):
    x, y = map(int, input().split())
    questions.append((x,y))

vTod  = dict(zip(v,list(range(1,7))))
dTov  = {v:k for k, v in vTod.items()}

for top, face in questions:
    top = vTod[top]
    face = vTod[face]
    right = d[(top,face)]
    right = dTov[right]
    print(right)
