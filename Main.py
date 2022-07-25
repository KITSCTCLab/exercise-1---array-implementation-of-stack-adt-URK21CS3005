import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        self.top=-1
        return self.top==-1

    def is_full(self):
        return self.top==self.size-1

    def push(self, data):
        if not self.is_full():
            self.top+=1
            x=int(input("Enter the data : "))
            self.items[self.top]=x

    def pop(self):
        if not self.is_empty():
            print("The deleted element is : ",self.items[self.top])
            self.items[self.top]=None
            self.top-=1

    def status(self):
        for i in range(self.to+1):
            print(self.items[i])

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
