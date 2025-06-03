import sys
import math

for line in sys.stdin:
    debut = 100000
    weeks = int(line)
    for i in range(weeks):
        debut = debut * 1.05
        debut = math.ceil(debut/1000)*1000
    print(debut)