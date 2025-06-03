import sys
import re
from collections import Counter

chardict = {chr(i):0 for i in range(97, 97+26)}
str1 = sys.stdin.read()
str1 = re.sub('[^a-z]', '', str1.lower())
counter = Counter(str1)
for word in counter:
    chardict[word] = counter[word]
charlist = sorted(chardict.items())
for x in charlist:
    print(x[0] + ' : ' + str(x[1]))