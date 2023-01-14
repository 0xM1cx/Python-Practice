from math import sqrt

def is_prime(n):
    flag = False
    if n == 1 or n == 0:
        flag = True
    elif n > 2:
        for i in range(2, round(sqrt(n))):
            if (n % i) == 0:
                flag = True
                break
            


    if flag:
        return False
    else:
        return True


print(is_prime(20021527))