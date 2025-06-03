
s=input()
if len(s)%2!=0:

    print("No")
else:
    bool=False
    for i in range(len(s)):
        if i%2==0:
            if s[i]!="h":

                print("No")
                bool=True
                break
        else:
            if s[i]!="i":
                print("No")

                bool=True
                break
    if bool is False:
        print("Yes")
