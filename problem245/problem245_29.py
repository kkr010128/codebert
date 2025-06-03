N = int(input())
S = input()
counter = 0
for i in range(0,N-2):
    if(S[i] == "A"):
        if(S[i+1] == "B"):
            if(S[i+2] == "C"):
                counter += 1
                
print(counter)