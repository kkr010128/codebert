line = int(input().split(" ")[0])
a_vec =[]
b_vec =[]
res = []



for i in range(line):
    #a_vec.append([int(x) for x in a_input[i].split(" ")])
    a_vec.append([int(x) for x in input().split(" ")])


for i in range(len(a_vec[0])):
    b_vec.append(int(input()))

for a_row in a_vec:
    c = 0
    for i, a_col in enumerate(a_row):
        c += a_col * b_vec[i]
    res.append(c)

for r in res:
    print(r)