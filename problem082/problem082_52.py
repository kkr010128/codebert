def solve(word1, word2):
	n1, n2 = len(word1), len(word2)
	res = []
	
	for i in range(n1 - n2 + 1):
		cur_s = word1[i : i + n2]
		res.append(sum(cur_s[j] != word2[j] for j in range(len(cur_s))))
	
	return min(res)
  
s = input()
p = input()
print(solve(s, p))