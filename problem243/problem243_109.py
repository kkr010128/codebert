n = int(input())
movies = {}

summize = 0
for i in range(n):
  input_str = input().split()
  summize += int(input_str[1])
  movies.setdefault(input_str[0], summize)

title = input()
print(summize - movies[title])