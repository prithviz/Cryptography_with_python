# Brute force

def bruteforce_decrypt(text):
    print "Decrypting...", text
    k = [i for i in range(1, 26)]
    for a in range(len(k)):
        print '\n'
        print 'Applying key=', k[a]
        result = []
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                r = chr((ord(char) - k[a] - 65) % 26 + 65)
            elif char.islower():
                r = chr((ord(char) - k[a] - 97) % 26 + 97)
            elif char.isdigit():
                r = chr((ord(char) - k[a] - 48) % 10 + 48)
            else:
                r = chr((ord(char) - k[a] - 32) % 16 + 32)
            result.append(r)
        print''.join(result)


print bruteforce_decrypt("EmtkwumBwOqbpcj")
