n = int(input())
s = input()

result = 0
for i in range(1000):
    i = str(i).zfill(3)
    # print(i)
    # print(s.find(i[0]), s.find(i[1]), s.find(i[2]))
    index0 = s.find(i[0])
    if -1 < index0:
        index1 = s.find(i[1], index0+1)
        if -1 < index1:
            index2 = s.find(i[2], index1+1)
            if -1 < index2:
                # print(i, 'あたり')
                result += 1

print(result)