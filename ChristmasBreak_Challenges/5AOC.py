def createStack():
    stack = []
    return stack

def push(stack, item):
    if type(item) == type([]):
        stack.extend(item)
    else:
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

push(stack1, ["[S]", "[M]", "[R]", "[N]", "[W]", "[J]", "[V]", "[T]"])
push(stack2, ["[B]", "[W]", "[D]", "[J]", "[Q]", "[P]", "[C]", "[V]"])
push(stack3, ["[B]", "[J]", "[F]", "[H]", "[D]", "[R]", "[P]"])
push(stack4, ["[F]", "[R]", "[P]", "[B]", "[M]", "[N]", "[D]"])
push(stack5, ["[H]", "[V]", "[R]", "[P]", "[T]", "[B]"])
push(stack6, ["[C]", "[B]", "[P]", "[T]"])
push(stack7, ["[B]", "[J]", "[R]", "[P]", "[L]"])
push(stack8, ["[N]", "[C]", "[S]", "[L]", "[T]", "[Z]", "[B]", "[W]"])
push(stack9, ["[L]", "[S]", "[G]"])


stacksDic = {
    "1": stack1,
    "2": stack2,
    "3": stack3,
    "4": stack4,
    "5": stack5,
    "6": stack6,
    "7": stack7,
    "8": stack8,
    "9": stack9
}


with open("5AOC.txt", "r") as file:
    for i in file:
        line = i.replace("\n", "")
        words = line.split(" ")
        
        moves = int(words[1])
        source = words[3]
        destination = words[5]

        for b in range(moves):
            crate = pop(stacksDic[source])
            push(stacksDic[destination], crate)


def displayStacks(stackDic):
    message = []
    for key in stackDic.keys():
        withBrackets = stackDic[key][-1]
        letter = withBrackets[1]
        message.append(letter)

    print(''.join(message))


displayStacks(stacksDic)        


