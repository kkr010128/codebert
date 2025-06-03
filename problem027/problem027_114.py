n = int(input())
p1, p2 = (0, 0), (100, 0)
ans_ls = [p1, p2]

def koch(d, p1, p2):
	if d == n:
		return
	s = (2/3*p1[0] + 1/3*p2[0], 2/3*p1[1] + 1/3*p2[1])
	t = (1/3*p1[0] + 2/3*p2[0], 1/3*p1[1] + 2/3*p2[1])

	R = [[1/2, -(3**(1/2))/2], [(3**(1/2))/2, 1/2]]
	u = (R[0][0]*(t[0] - s[0]) + R[0][1]*(t[1] - s[1]) + s[0],
		R[1][0]*(t[0] - s[0]) + R[1][1]*(t[1] - s[1]) + s[1])
	ans_ls.extend([s, u, t])

	koch(d + 1, p1, s)
	print(*s)
	koch(d + 1, s, u)
	print(*u)
	koch(d + 1, u, t)
	print(*t)
	koch(d+1, t, p2)

print(*p1)
koch(0, p1, p2)
print(*p2)
