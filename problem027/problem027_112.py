
n = input()

def koch(n,p1,p2):
    s = [0] * 2 
    t = [0] * 2 
    u = [0] * 2 
    if n == 0:
        return 0
    s[0] = (2.00 * p1[0] + 1.00 * p2[0]) / 3.00
    s[1] = (2.00 * p1[1] + 1.00 * p2[1]) / 3.00
    t[0] = (1.00 * p1[0] + 2.00 * p2[0]) / 3.00
    t[1] = (1.00 * p1[1] + 2.00 * p2[1]) / 3.00
    u[0] = (t[0] - s[0]) * (1.00 / 2.00) - (t[1] - s[1]) * (3.00**0.5 / 2.00) + s[0] 
    u[1] = (t[0] - s[0]) * (3.00**0.5 / 2.00) + (t[1] - s[1]) * (1.00 / 2.00) + s[1]    


    koch(n-1, p1, s)
    print "{0:.10f}".format(s[0]),"{0:.10f}".format(s[1])
    koch(n-1, s, u)
    print "{0:.10f}".format(u[0]),"{0:.10f}".format(u[1])
    koch(n-1, u, t)
    print "{0:.10f}".format(t[0]),"{0:.10f}".format(t[1])  
    koch(n-1, t, p2)




start = [0.00,0.00]
goal = [100.00,0.00]
print "{0:.10f}".format(start[0]),"{0:.10f}".format(start[1])
koch(n,start,goal)
print "{0:.10f}".format(goal[0]),"{0:.10f}".format(goal[1])