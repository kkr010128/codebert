y,x = [int(x) for x in input().split()]
even = "#." * 151
odd  = ".#" * 151
while(x > 0 or y > 0):
    for i in range(y):
        if(i % 2 == 0):
            print(even[:x])
        else:
            print(odd[:x])
    print()          
    y,x = [int(x) for x in input().split()]