m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())

end = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if d1 == end[m1-1]:
    print(1)
else:
    print(0)