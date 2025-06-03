n, k = map(int, input().split())
prime_mod = 10**9+7
countgcd = [0]*k
for idx in range(k, 0, -1):
  num_multiples = k//idx
  num_sequences = pow(num_multiples, n, prime_mod)
  overcount = sum(countgcd[j*idx-1] for j in range(2, num_multiples+1))
  overcount = overcount%prime_mod
  countgcd[idx-1] = (num_sequences-overcount)%prime_mod
  # print(idx, num_multiples, num_sequences, overcount, num_sequences-overcount)
final_sum = 0
for idx in range(1, k+1):
  final_sum = (final_sum + idx*countgcd[idx-1])%prime_mod
print(final_sum)