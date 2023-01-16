def create_stack():
    stack = []
    return stack


def push(stack, item):
    stack.append(item)

def pop(stack):
    if len(stack) > 0:
        return stack.pop()




s = create_stack()

push(s, 1)
push(s, 2)
push(s, 3)
push(s, 4)
push(s, 5)
push(s, 6)

print(s)
print(pop(s))
print(s)