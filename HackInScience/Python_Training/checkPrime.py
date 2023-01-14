def is_prime(n):

    if n == 1 or n == 0 or n == 2:
        return False
    elif n > 2:
        for i in range(2, n):
            if n % i == 0:
                return False
            else: 
                return True

print(is_prime(9))