from sys import stdin
import re

W = stdin.readline().rstrip()
T = stdin.read().replace("END_OF_TEXT", ".").lower()
T = re.split(",|\n| ", T)
print(len([x for x in T if x == W]))
