inData = int(input())

seqData = list(range(1,inData+1,1))
outData = [0] * inData
for thisData in seqData:
    if thisData == inData:
        if thisData%3 == 0 or thisData%10==3:
            print(" "+str(thisData))
        else:
            for i in range(5):
                i=i+1
                over =  10 ** i
                tmp = thisData/over
                if int(tmp % 10) == 3:
                    print(" "+str(thisData))
                    break
                else:
                    pass
            print("")
    else:
        if thisData%3 == 0 or thisData%10==3:
            print(" "+str(thisData), end = "")
        else:
            for i in range(5):
                i=i+1
                over =  10 ** i
                tmp = thisData/over
                if int(tmp % 10) == 3:
                    print(" "+str(thisData), end = "")
                    break
                else:
                    pass
