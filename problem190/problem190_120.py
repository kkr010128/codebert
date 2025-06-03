s = input()
n = len(s)
s_re =s[::-1]
s_first = s[:(n-1)//2]
s_first_re = s_first[::-1]
s_second = s[(n+3)//2-1:]
s_second_re = s_second[::-1]

print(['No','Yes'][s == s_re and s_first==s_first_re and s_second == s_second_re])