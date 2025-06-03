a, b = eval(input().replace(' ', ','))
print("a {} b".format("<" if a < b else ">" if a > b else "=="))