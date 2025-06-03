a=raw_input()
debt = 100000
for i in range(int(a)):
    debt += debt/20
    b=debt%1000
    if b > 0:
	debt += 1000-b
print debt