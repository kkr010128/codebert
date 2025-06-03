ina = input()
inb = input()

l = int(ina)
cw1 = inb.count("W")
cw2 = inb[-cw1:].count("W")
print(cw1-cw2)