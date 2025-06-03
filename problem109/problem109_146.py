N = int(input())
L = []
for i in range(N):
  L.append(input())

print("AC x "+str(L.count('AC'))+
"\nWA x "+str(L.count('WA'))+
"\nTLE x "+str(L.count('TLE'))+
"\nRE x "+str(L.count('RE')))