class Dictionary_class:
    def __init__(self):
        self.dic = set()

    def insert(self, str):
        self.dic.add(str)

    def find(self, str):
        if str in self.dic:
            return True
        else:
            return False

n = int(input())
answer = ""
dic = Dictionary_class()
for i in range(n):
    instruction = input().split()
    if instruction[0] == "insert":
        dic.insert(instruction[1])
    elif instruction[0] == "find":
        if dic.find(instruction[1]):
            answer += "yes\n"
        else:
            answer += "no\n"
print(answer, end = "")