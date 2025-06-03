import sys

# C - Walking Takahashi
X, K, D = map(int, input().split())

if D * K <= abs(X):
	print(abs(X) - D * K)
else:
	distance = abs(X) % D

	# 残りの移動回数
	count = K - (abs(X) // D)

	if count % 2 == 1:
		print(abs(D - distance))
	else:
		print(distance)