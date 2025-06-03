
n = raw_input()
num = raw_input()
array = []
array = num.strip().split(" ")
int_array = map(int, array)

for i in range(1, int(n)):
    array = map(str, int_array)
    print " ".join(array)
    v = int_array[i]
    j = i - 1
    while j >= 0 and int_array[j] > v:
        int_array[j + 1] = int_array[j]
        j -= 1
    int_array[j + 1] = v
array = map(str, int_array)
print " ".join(array)