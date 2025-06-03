n=int(input())
c=list(input())

from collections import Counter
cnt=Counter(c)
num_of_red = cnt['R']
num_of_white_replace_to_red = c[:num_of_red].count('W')
print(num_of_white_replace_to_red)