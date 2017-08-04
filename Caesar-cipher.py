# caesar cipher

def caesar_encrypt(text):
    result = ""
    k = 3
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + k - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + k - 97) % 26 + 97)
        elif char.isdigit():
            result += chr((ord(char) + k - 48) % 10 + 48)
        else:
            result += chr((ord(char) + k - 32) % 16 + 32)
    return result


def caesar_decrypt(text):
    result = ""
    k = 3
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - k - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - k - 97) % 26 + 97)
        elif char.isdigit():
            result += chr((ord(char) - k - 48) % 10 + 48)
        else:
            result += chr((ord(char) - k - 32) % 16 + 32)
    return result


pt = 'It is simple transposition cipher'
a = caesar_encrypt(pt)
b = caesar_decrypt(a)
print a, ":Ciphertext"
print b, ":plaintext"
