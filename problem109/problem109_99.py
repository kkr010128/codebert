n = int(input())
l = {'AC':0,'WA':0,'TLE':0,'RE':0}
for i in range(n):
  l[input()] += 1
print('AC x',l['AC'])
print('WA x',l['WA'])
print('TLE x',l['TLE'])
print('RE x',l['RE'])