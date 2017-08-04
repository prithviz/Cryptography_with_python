# Fermet's theorem

from random import randint


def isProbablyPrime(n, k=5):
    if (n < 2):
        return False
    output = True
    for i in range(0, k):
        a = randint(1, n - 1)
        if (pow(a, n - 1, n) != 1):
            return False
    return output


# tests
print isProbablyPrime(1)  # False
print isProbablyPrime(2)  # True
print isProbablyPrime(3)  # True
print isProbablyPrime(4)  # False



# Let's multiply large prime numbers by themselves and test their primality (should be False)
print isProbablyPrime(32416190071 * 32416190071)
print isProbablyPrime(
    22953686867719691230002707821868552601124472329079 * 22953686867719691230002707821868552601124472329079)