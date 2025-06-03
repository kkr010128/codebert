import sys

S = input()

if not ( S == 'ABC' or S == 'ARC' ): sys.exit()

print('ABC') if S == 'ARC' else print('ARC')