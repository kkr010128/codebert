import sys


def calc_cell(x, y):
	return '.' if (x + y) % 2 else '#'


def print_chessboard(height, width):
	for y in range(height):
		l = []
		for x in range(width):
			l.append(calc_cell(x, y))
		print ''.join(l)

if __name__ == '__main__':
	while True:
		h, w = map(int, sys.stdin.readline().split())
		print_chessboard(h, w)

		if not h or not w:
			break

		print