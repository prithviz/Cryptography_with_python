# Diffie hellman key Exchange and performing caesar cipher

from random import getrandbits

g = 2
prime = 7919
bits = 32

# Generate Alice's secret and public keys (a,A)
a = getrandbits(bits)
A = pow(g, a, prime)
# Generate Bob's secret and public keys (b,B)
b = getrandbits(bits)
B = pow(g, b, prime)

# Generate the shared secrets
# shared key= pow(public key,secret key, prime)
s1 = pow(A, b, prime)
s2 = pow(B, a, prime)

if (s1 == s2):
    print("Shared secrets match: ", s1)
else:
    print("Shared secrets not match: ", s1)
'''We are getting same key(randomly generated) at both side, we will use it in 
caesar cipher algorithm.'''


# code for caeser cipher
def encrypt(text, k):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + k - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + k - 97) % 26 + 97)
        elif (char.isdigit()):
            result += chr((ord(char) + k - 48) % 10 + 48)
        else:
            result += chr((ord(char) + k - 32) % 16 + 32)
    return result


def dycrypt(text1, k1):
    result1 = ""
    for i in range(len(text1)):
        char = text1[i]
        if (char.isupper()):
            result1 += chr((ord(char) - k1 - 65) % 26 + 65)
        elif (char.islower()):
            result1 += chr((ord(char) - k1 - 97) % 26 + 97)
        elif (char.isdigit()):
            result1 += chr((ord(char) - k1 - 48) % 10 + 48)
        else:
            result1 += chr((ord(char) - k1 - 32) % 16 + 32)
    return result1


text = raw_input("Enter Msg:")
text1 = encrypt(text=text, k=s1)
# here key will be same as we received in deffie hellman key exchange technique.
print "Encrypted:", text1
text2 = dycrypt(text1=text1, k1=s1)
print "Decrypted:", text2
