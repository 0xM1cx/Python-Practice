def questionOne():
    '''OUTPUT
    0
    2
    4
    6
    8'''
    for i in range(10):
        if i % 2 == 0:
            print(i)


def getThis():
	return "INTEL"


def main():
	uInput = getThis()
	return uInput + "!!!"

print(main())
