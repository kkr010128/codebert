def koch_curve(points, n):
    if n == 0:
        return points
    result = []
    for i in range(len(points) - 1):
        x = points[i+1][0] - points[i][0]
        y = points[i+1][1] - points[i][1]
        s = [points[i][0]+x/3, points[i][1]+y/3]
        t = [points[i][0]+2*x/3, points[i][1]+2*y/3]
        u_x = t[0]/2 - t[1]*(3**0.5/2) + s[0]/2+(3**0.5)*s[1]/2
        u_y = t[0]*3**0.5/2 + t[1]/2 + s[1]/2-(3**0.5)*s[0]/2
        u = [u_x, u_y]
        result.extend([points[i], s, u, t])
    result.append(points.pop())
    return koch_curve(result, n - 1)

n = int(input())
for point in koch_curve([[0.0, 0.0], [100.0, 0.0]], n):
    print(*map(str, point))