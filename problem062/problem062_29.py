while True:
    number = input()
    if(number == "0"): 
        break
    print(sum([int(a) for a in list(number)]))