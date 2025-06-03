import sys
input = sys.stdin.readline

# A - Table Tennis Training
def move_left():
	return A + (B-A-1)//2


def move_right():
	return  N - B + 1 + (B-A-1)//2	


N, A, B = map(int, input().split())

if (B-A) % 2 == 0:
	print(int((B-A)//2))
else:
	l = move_left()
	r = move_right()
	print(min(l, r))