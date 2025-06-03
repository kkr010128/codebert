W = input()
T = input()
count = 0
while T != 'END_OF_TEXT':
    T = T.lower().split()
    count += T.count(W.lower())
    T = input()
print(count)