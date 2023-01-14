def is_prime(n):
    flag = 0;
    if n == 1 or n == 0 or n == 2:
        return 1
    elif n > 2:
        for i in range(2, n):
            if n % i == 0:
                flag = 1
            else: 
                flag = 0


    if flag == 0:
        return True
    else:
        return False

        
print(is_prime(9))