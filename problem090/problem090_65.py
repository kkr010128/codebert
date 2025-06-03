S = input()

if 'RRR' in S: ANS = 3
elif 'RR' in S: ANS = 2
elif 'RS' in S: ANS = 1
elif 'SR' in S: ANS = 1
elif 'SSS' in S: ANS = 0

print(ANS)