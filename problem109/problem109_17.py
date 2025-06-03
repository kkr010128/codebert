N = int(input())
s = [input() for i in range(N)]
'''
for v in ["AC", "WA", "TLE", "RE"]:
    print("{0} x {1}".format(v, s.count(v)))
'''

print("AC x",s.count("AC"))
print("WA x",s.count("WA"))
print("TLE x",s.count("TLE"))
print("RE x",s.count("RE"))