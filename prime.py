from pydoc import ispackage


def is_prime(n): 
    if n < 2: 
        return False
    for i in range(2, n+1, 1): 
        if i != 1 and i != n: 
            if n % i == 0: 
                return False

    return True

print(is_prime(100))