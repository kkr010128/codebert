N = int(input())
 
dict = {}
strings = []
for i in range(N):
    x = input()
    if x in dict.keys():
        dict[x] += 1
    else:
        dict[x] = 1
 
maximum = 1
for i in dict:
    maximum = max(maximum,dict[i])
 
for word in dict:
    if dict[word] == maximum:
        strings.append(word)
strings.sort()
for word in strings:
    print(word)