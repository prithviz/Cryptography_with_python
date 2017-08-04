# Euclidean Algorithm

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print gcd(123211, 1432), 'euclidean algorithm'


# Extended Euclidean Algorithm
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


print egcd(1432, 1211), 'extended euclidean algorithm'


# Inverse using Extended Euclidean Algorithm
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


print modinv(1432, 1211), 'Multiplicative Inverse'
