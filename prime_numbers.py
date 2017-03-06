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

    prime_numbers = []

    # loop from 2 (since that is the first prime number) to `n`
    # for each number check if it is a prime number

    for num in range(2, n+1):
        if is_prime_number(num):
            prime_numbers.append(num)

    return prime_numbers