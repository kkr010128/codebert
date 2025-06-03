import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
import sys

# sys.stdout.write(str(n)+"\n")
MODULO = 1000000007
# INF = 1e18+10

def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a

n = int(input())

a_b = [() for i in range(n)]
m_b_a = [() for i in range(n)]

# a_b_value_indices = {}
# m_b_a_value_indices = {}

a_b_value_count = {}
m_b_a_value_count = {}

a_b_value_rep = {}
m_b_a_value_rep = {}

used = [False for _ in range(n)]
zeroes = 0
is_zero = [False for _ in range(n)]

for i in range(n):
	a, b = map(int, input().split())

	if a == 0 and b == 0:
		zeroes += 1
		used[i] = True
		is_zero[i] = True
	else:
		if a == 0:
			a_b[i] = (0, 1)
			m_b_a[i] = (1, 0)
		elif b == 0:
			a_b[i] = (1, 0)
			m_b_a[i] = (0, 1)
		else:
			neg = False
			if a*b < 0:
				neg = True
			d = gcd(abs(a), abs(b))
			a = abs(a) // d
			b = abs(b) // d

			if neg:
				a_b[i] = (-a, b)
				m_b_a[i] = (b, a)
			else:
				a_b[i] = (a, b)
				m_b_a[i] = (-b, a)

		a_b_value_count[a_b[i]] = a_b_value_count.get(a_b[i], 0) + 1
		# a_b_value_indices[a_b[i]] = a_b_value_indices.get(a_b[i], []) + [i]
 
		m_b_a_value_count[m_b_a[i]] = m_b_a_value_count.get(m_b_a[i], 0) + 1
		# m_b_a_value_indices[m_b_a[i]] = m_b_a_value_indices.get(m_b_a[i], []) + [i]
		if a_b[i] not in a_b_value_rep:
			a_b_value_rep[a_b[i]] = i
		if m_b_a[i] not in m_b_a_value_rep:
			m_b_a_value_rep[m_b_a[i]] = i

ans = 1
for i in range(n):
	if not is_zero[i] and not used[a_b_value_rep[a_b[i]]]:
		# if not connected
		if a_b[i] not in m_b_a_value_count:
			ans *= pow(2, a_b_value_count[a_b[i]], MODULO)
			ans %= MODULO
			used[a_b_value_rep[a_b[i]]] = True
			# for j in a_b_value_indices[a_b[i]]:
			# 	used[j] = True
		else:
			s = a_b_value_count[a_b[i]]
			t = m_b_a_value_count[a_b[i]]
			ans *= ((1*pow(2, s, MODULO) + 1*pow(2, t, MODULO) -1) % MODULO)
			ans %= MODULO

			used[a_b_value_rep[a_b[i]]] = True
			used[m_b_a_value_rep[a_b[i]]] = True
			# for j in m_b_a_value_indices[a_b[i]]:
			# 	used[j] = True
 
			# used_a_b_keys.add(a_b_key)
			# used_a_b_keys.add(-1/a_b_key)
 
 
# -1 is for empty
print((ans-1+zeroes) % MODULO)