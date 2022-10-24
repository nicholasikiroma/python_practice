
def isPrime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    
    return True

def getPrime(max_number):
    list_of_prime = []
    for num in range(2, max_number + 1):
        if isPrime(num):
            list_of_prime.append(num)
    return list_of_prime

max_number = int(input("Enter the max number: "))
prime_numbers = getPrime(max_number)
print(prime_numbers)
