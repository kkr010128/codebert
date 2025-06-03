def koch_curve(point1, point2, N):
    if N == 0:
        print('{:8f} {:8f}'.format(point1[0], point1[1]))
        return
    pointS = ((2 * point1[0] + point2[0]) / 3,
              (2 * point1[1] + point2[1]) / 3)
    pointT = ((point2[0] - point1[0]) / 2 - (point2[1] - point1[1]) / 3.46410161514 + point1[0],
              (point2[0] - point1[0]) / 3.46410161514 + (point2[1] - point1[1]) / 2 + point1[1])
    pointU = ((point1[0] + 2 * point2[0]) / 3,
              (point1[1] + 2 * point2[1]) / 3)
    if N > 1:
        koch_curve(point1, pointS, N - 1)
        koch_curve(pointS, pointT, N - 1)
        koch_curve(pointT, pointU, N - 1)
        koch_curve(pointU, point2, N - 1)
    else:
        print('{:8f} {:8f}'.format(point1[0], point1[1]))
        print('{:8f} {:8f}'.format(pointS[0], pointS[1]))
        print('{:8f} {:8f}'.format(pointT[0], pointT[1]))
        print('{:8f} {:8f}'.format(pointU[0], pointU[1]))


N = int(input())
koch_curve((0.0, 0.0), (100.0, 0.0), N)
print('100.00000000 0.00000000')
