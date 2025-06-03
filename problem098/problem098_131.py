n=int(input())
s=input()

rcnt=s.count("R")
wcnt=s[:rcnt].count("W")
print(wcnt)