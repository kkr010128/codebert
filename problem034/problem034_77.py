#coding: utf-8

tfr = ((1, 2, 4, 3), (0, 3, 5, 2), (0, 1, 5, 4),
(0, 4, 5, 1), (0, 2, 5, 3), (1, 3, 4, 2))

label = list(map(int, input().split()))
q = int(input())
for i in range(q):
    t, f = map(int, input().split())
    idxt = label.index(t)
    idxf = label.index(f)
    idxr = tfr[idxt].index(idxf) + 1
    if idxr == 4:
        idxr = 0
    print(label[tfr[idxt][idxr]])
