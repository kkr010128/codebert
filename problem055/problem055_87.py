line = int(input())
nums = [[[0 for x in range(0, 10)] for x in range(0, 3)] for x in range(0, 4)]
input1 = []
for i in range(line):
    input1.append(input())


for e in input1:
    efbv =  e.split(" ")
    e_b, e_f, e_r, e_v = map(int, efbv)
    nums[e_b - 1][e_f - 1][e_r -1] += e_v

for b in range(4):
    for f in range (3):
        print(" " + " ".join(map(str, nums[b][f])))
    if b != 3: print("#" * 20)