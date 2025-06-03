import sys

#fin = open("test.txt", "r")
fin = sys.stdin

n = int(fin.readline())

taros_score = 0
hanakos_score = 0
winner_points = 3
draw_points = 1

for i in range(n):
	s0, s1 = fin.readline().split()

	if s0 > s1:
		taros_score += winner_points
	elif s0 < s1:
		hanakos_score += winner_points
	else:
		taros_score += draw_points
		hanakos_score += draw_points

print(taros_score, hanakos_score)