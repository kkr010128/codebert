while True:
    string = input()
    if string == "-":
        break
    times = int(input())
    for i in range(times):
        cut=int(input())
        string = string[cut:]+string[:cut]
        
    print(string)