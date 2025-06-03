def Next(): return input()
def NextInt(): return int(Next())
def NextInts(): return map(int,input().split())
def Nexts(): return map(str,input().split())
def NextIntList(): return list(map(int,input().split()))
def RowInts(n): return [input() for i in range(n)]

s = input()
if s[-1] == 's':
    s = s + 'es'
else:
    s = s + 's'
print(s)