cnt = 0
n = int(raw_input())
A = [int(raw_input()) for _ in range(n)]
G = [1] if n < 5 else [1, 4]
while G[-1]*3+1 <= n/5: G.append(G[-1]*3+1)
G.reverse()

def insersionSort(g):
	global cnt
	for i in range(g, n):
		v = A[i]
		j = i - g
		while j >= 0 and A[j] > v:
			A[j+g] = A[j]
			j = j - g
			cnt += 1
		A[j+g] = v

def shellSort():
	for g in G:
		insersionSort(g)

shellSort()
print len(G)
print " ".join(map(str, G))
print cnt
print "\n".join(map(str, A))