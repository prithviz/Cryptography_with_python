# Hill Cipher

def hill(message, key, decrypt=False):
    from math import sqrt
    n = int(sqrt(len(key)))
    if n * n != len(key):
        raise Exception("Invalid key length, should be square-root-able like")

    alpha = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.?,-;|'
    print "[ALPHA LENGTH]: ", len(alpha)
    tonum = dict([(alpha[i], i * 1) for i in range(len(alpha))])

    # Pad the message with spacess if necessary(adds extra symbol '|')
    if len(message) % n > 0:
        message += '|' * (n - (len(message) % n))

    # Construct our key matrix
    keylist = []
    for a in key:
        keylist.append(tonum[a])

    keymatrix = []
    for i in range(n):
        keymatrix.append(keylist[i * n: i * n + n])

    from numpy import matrix
    from numpy import linalg

    keymatrix = matrix(keymatrix).round().T

    if decrypt:
        # finding determinant with round value
        determinant = linalg.det(keymatrix).round()
        # deteminant must be non zero and not divisible by Alpha's size
        if determinant == 0:
            raise Exception("Determinant ZERO, CHANGE THE KEY!")
        elif determinant % len(alpha) == 0:
            raise Exception("Determinant divisible by ALPHA LENGTH, CHANGE THE KEY!")
        # inverse matrix of keymatrix
        inverse = []
        # making of keymatrix's inverse * determinant with round value
        keymatrix = matrix(keymatrix.getI() * determinant).round()
        invdeterminant = 0
        for i in range(10000):
            if (determinant * i % len(alpha)) == 1:
                invdeterminant = i
                break

        print "[INVERTED DETERMINANT]", invdeterminant

        # Modular multiplicative inverse
        for row in keymatrix.getA() * invdeterminant:
            newrow = []
            for i in row:
                newrow.append(i.round() % len(alpha))
            inverse.append(newrow)

        keymatrix = matrix(inverse)

        print "[DECIPHERING]: ", message
    else:
        print "[ENCIPHERING]: ", message

    print "[MATRIX]\n", keymatrix

    # Main loop for Mapping from alpha
    from string import join
    out = ''
    for i in range(len(message) / n):
        # lst will contain message's key's value one by one and coverted to matrix
        lst = matrix([[tonum[a]] for a in message[i * n:i * n + n]])
        # result is multiplication of two matrix
        result = keymatrix * lst
        # following statement will does modulo with length of alpha {(%43) to get result in range of 0 to 42}
        # on result matrix and creates array that mapped values from alpha
        out += ''.join([alpha[int(result.A[j][0]) % len(alpha)] for j in range(len(result))])
    return out


key = "XBPDEFGPIJKLMNOO"
msg = "GITHUB ISS"

cipherText = hill(msg, key)
print'#' * 40
print "[CIPHERED TEXT]: |%s|\n" % cipherText

decipherText = hill(cipherText, key, True)

'''if decipherText.find('|') > -1:
    decipherText = decipherText[:decipherText.find('|')]'''
print'#' * 40
print "[DECIPHERED TEXT]: |%s|\n" % decipherText
print'#' * 40

