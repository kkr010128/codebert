# coding: utf-8
# Here your code !

# coding: utf-8
# Here your code !

def func():
    try:
        line = input()
    except:
        return inputError()
        
    (buildings,floors,rooms,maxnumber)=(4,3,10,9)
    tenants=[ [ [0 for i in range(rooms)] for j in range(floors)] for k in range(buildings)]
   
    while(True):
        try:
            line=input().rstrip()
            info=line.split(" ")
            (building, floor, room, number)=( int(info[0])-1, int(info[1])-1, int(info[2])-1, int(info[3]) )
        except EOFError:
            break
        except:
            return inputError()
        
        if( (building >= 0) and (building < buildings) ):
            if( (floor >= 0) and (floor < floors) ):
                if( (room >= 0) and (room < rooms) ):
                    if( (tenants[building][floor][room]+number >= 0) and (tenants[building][floor][room]+number < maxnumber+1) ): 
                        tenants[building][floor][room] += number
                    else:
                        return inputError()
                else:
                    return inputError()
            else:
                return inputError()
        else:
            return inputError()
    
    result=""
    for i in range(buildings):
        for j in range(floors):
            for k in range(rooms):
                result += " {0}".format(tenants[i][j][k])
            result += "\n"
        if(i+1 < buildings):
            result+="#"*rooms*2+"\n"
            
    print(result.rstrip())        
    
def inputError():
    print("input error")
    return -1


func()