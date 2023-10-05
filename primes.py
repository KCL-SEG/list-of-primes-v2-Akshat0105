"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def isprime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    cont = 0
    for i in range(1,num+1):
     if num % i ==0:
        cont +=1
    return cont == 2  
            
def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be positive number")
    list = []
    num = 2
    while len(list) < number_of_primes:
        if isprime(num):
            list.append(num)
        num +=1    
    return list
