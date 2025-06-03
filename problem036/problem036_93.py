input = raw_input()
input_items = input.split()
a = int(input_items[0])
b = int(input_items[1])
area = a * b
length = 2*a + 2*b
print str(area) + ' ' + str(length)