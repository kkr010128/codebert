N = int(input())
words = list(input())
ct_R = words.count('R')
ct_W = words.count('W')
a = words[0:ct_R]
W_in_a_count = a.count('W')
print(W_in_a_count)
