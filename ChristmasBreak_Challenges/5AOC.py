def createStack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()


stack1 = createStack()
stack2 = createStack()
stack3 = createStack()
stack4 = createStack()
stack5 = createStack()
stack6 = createStack()
stack7 = createStack()
stack8 = createStack()
stack9 = createStack()

with open("5AOC.txt", "r") as file:
    for i in file:
        line = i.replace("\n", "")

        
