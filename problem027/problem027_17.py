# -*- coding: utf-8 -*-
import math

class KochCurve(object):
	x = 0.0
	y = 0.0

	# ?§£???
	def koch(self, n, a, b):
		if n == 0:
			return 

		s = KochCurve()
		t = KochCurve()
		u = KochCurve()
		th = math.pi * 60.0 / 180.0

		s.x = (2.0 * a.x + 1.0 * b.x) / 3.0
		s.y = (2.0 * a.y + 1.0 * b.y) / 3.0
		t.x = (1.0 * a.x + 2.0 * b.x) / 3.0
		t.y = (1.0 * a.y + 2.0 * b.y) / 3.0
		u.x = (t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x
		u.y = (t.x - s.x) * math.sin(th) + (t.y - s.y) * math.cos(th) + s.y
		
		KochCurve().koch(n - 1, a, s)
		msg = "%.8f %.8f" % (s.x, s.y)
		print(msg)
		KochCurve().koch(n - 1, s, u)
		msg = "%.8f %.8f" % (u.x, u.y)
		print(msg)
		KochCurve().koch(n - 1, u, t)
		msg = "%.8f %.8f" % (t.x, t.y)
		print(msg)
		KochCurve().koch(n - 1, t, b)


if __name__ == '__main__':
	a = KochCurve()
	b = KochCurve()

	n = int(input())

	a.x = 0
	a.y = 0
	b.x = 100
	b.y = 0

	msg = "%.8f %.8f" % (a.x, a.y)
	print(msg)
	KochCurve().koch(n, a, b)
	msg = "%.8f %.8f" % (b.x, b.y)
	print(msg)