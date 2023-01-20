'''Create another program "power.py", that accepts two positive integers x and a.
The output will be the answer to the power formula shown below. Do not use the built-in exponent operator. Use loops and multiplication instead.'''

def exerciseOne():
    x = int(input("First Integer: "))
    a = int(input("Second Integer: "))
    b = x
    # Formula => p = x^a where a is the exponent find 'p'
    for i in range(a-1):
        x *= b

    print(f"The answer is: {x}")
def exerciseTwo():
    for i in range(1, 10):
        for b in range(1, i):
            print("*", end="")
        print("")

    for y in range(10, 1):
        for z in range(y, 1):
            print("*", end="")
        print("")

def lambdaPractice():
    greetUser = lambda name : print(f"Welcome {name}")
    greetUser("Shawn")

    # sort an list of tuples by their second element using
    # lamda function    
    tuple_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
    tuple_list.sort(key=lambda i : i[1]) # instructs Python to sort list of tuples by the second element
    print(tuple_list)

    # sort a list of dictionanries using a lambda function
    dict_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
    sorted_dictList = sorted(dict_list, key=lambda a: int(a['model']))
    print(dict_list)

    
    
lambdaPractice()