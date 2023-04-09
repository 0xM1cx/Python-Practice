
# name = input()
# hour_rendered = int(input())
# loan = int(input())
# health_insurance = input()


# def GrossSalary():
# 	pass


# def SalaryDeduction():
# 	pass

# def NetSalary():
# 	pass
def tupPractice():
	my_tup = (1, 2)
	
	print(my_tup.index(2))
	

def convert_listToTuple():
	my_list = [1,2, 3, 4]
	print(my_list)
	print(type(my_list))
	my_tup = tuple(my_list)
	print(my_tup)
	print(type(my_tup))


def addItem_toTuple():
	tup = (1, 2)
	print(tup)
	tup[-1] = 3
	print(tup)


def addOne(x):
	x += 1
	return x

def stutter(word):
	first_twoLetters = word[0:2]
	return f"{first_twoLetters}...{first_twoLetters}...{word}"


# print(f"I {stutter('Love')} you {stutter('Zyra')}")


def findDiscount(price, discount):
	discount = discount / 100

	return round(price * discount, 2)

# print(findDiscount(1500, 50))
# print(findDiscount(89, 20))
# print(findDiscount(100, 75))


def incrementByOne(x):
	x += 1
	return x 

# print(incrementByOne(1))
# print(incrementByOne(-1))
# print(incrementByOne(-4))


def minToSec(mins):
	return mins * 60

# print(minToSec(5))


def GetAreaOfTraianlge(h, b):
	area = (h * b)//2
	return area

# print(f'GetAreaOfTraianlge(3, 2) -> {GetAreaOfTraianlge(3, 2)}')
# print(f"GetAreaOfTraianlge(7, 4) -> {GetAreaOfTraianlge(7, 4)}")
# print(f"GetAreaOfTraianlge(10, 10) -> {GetAreaOfTraianlge(10, 10)}")
