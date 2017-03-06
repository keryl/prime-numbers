def is_prime_number(num):

    if num < 2: # prime numbers start from 2
        return False

    # loop through all numbers less `than` num and return true if it is not divisible by any of them

    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

def get_prime_numbers(n):
    pass