# playfair cipher

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
         'X', 'Y', 'Z']

"""
Function: key_key()
Brief: Receives the key as input from the user. Handles valid characters and special cases.
Parameter: None
Return: Returns the key entered by the user.
"""


def get_key():
    k = raw_input().upper()
    key = []
    for char in k:
        if char in alpha and char not in key:  # add the character to the matrix if it's valid and not already in the matrix
            key.append(char)
        elif char is "J":  # handle the case when the letter J appears in the key
            key.append("I")
    for char in alpha:
        if char not in key:  # add the rest of the alphahet not appearing in the key to the matrix
            key.append(char)
    return key


"""
Function: gen_matrix(key)
Brief: Generates a Playfair matrix with the given key.
Parameter: key - The key to use for generating a Playfair matrix.
Return: Returns the keyed Playfair matrix.
"""


def gen_matrix(key):
    matrix = []
    counter = 0
    if key == '':  # create a blank matrix
        for xcounter in xrange(5):
            x = []
            for ycounter in xrange(5):
                x.append(alpha[counter])
                counter += 1
            matrix.append(x)
    else:  # create a keyed matrix
        for xcounter in xrange(5):
            x = []
            for ycounter in xrange(5):
                x.append(key[counter])
                counter += 1
            matrix.append(x)
    return matrix


"""
Function: print_matrix(matrix)
Brief: Prints the given Playfair matrix.
Parameter: matrix - The Playfair matrix to print out.
Returns: None.
"""


def print_matrix(matrix):
    for counter in xrange(5):
        print "%c %c %c %c %c" % (
            matrix[counter][0], matrix[counter][1], matrix[counter][2], matrix[counter][3], matrix[counter][4])
    print "\n"


"""
Fucntion: get_message()
Brief: Receives a message an input from the user. Handles valid characters and special cases.
Parameter: None
Return: Returns the resulting message.
"""


def get_message():
    m = raw_input()
    m2 = []
    for char in m.upper():
        if char in alpha:  # handle valid characters in the message
            m2.append(char)
        elif char == "J":  # handle the case when "J" appears in the message
            m2.append("I")
        elif char == ".":  # swap out the period with an x, for convenience
            m2.append("X")
    return ''.join(m2)


"""
Function encrypt(message, key_matrix)
Brief: Performs encryption of the given message with the keyed Playfair matrix.
Parameter: message - The message to perform encryption on.
Parameter: key_matrix - The keyed Playfair matrix to use for encryption.
Return: Returns nothing, the resulting ciphertext is printed at the end
	of the function.
"""


def encrypt(message, key_matrix):
    coords = []
    ciphertext = []
    digraphs = parse_message(message)

    for d in digraphs:
        swap = []
        temp = []
        coords = get_coords(d, key_matrix)
        if coords[0][0] == coords[1][0]:  # digraph lies on same x axis
            x, y = ((coords[0][0], (coords[0][1] + 1) % 5))
            swap.append((x, y))
            x, y = ((coords[1][0], (coords[1][1] + 1) % 5))
            swap.append((x, y))
        elif coords[0][1] == coords[1][1]:  # digraph lies on same y axis
            x, y = (((coords[0][0] + 1) % 5), coords[0][1])
            swap.append((x, y))
            x, y = (((coords[1][0] + 1) % 5), coords[1][1])
            swap.append((x, y))
        else:  # digraph lies on different x & y axis
            swap.append((coords[0][0], coords[1][1]))
            swap.append((coords[1][0], coords[0][1]))

        for x, y in swap:
            ciphertext.append(key_matrix[x][y])

    print "Your encrypted message is: %s " % ''.join(ciphertext)


"""
Function decrypt(message, key_matrix)
Brief: Performs decryption of the given message with the keyed Playfair matrix.
Parameter: message - The message to perform decryption on.
Parameter: key_matrix - The keyed Playfair matrix to use for decryption.
Return: Returns nothing, the resulting plaintext is printed at the end of the function.
"""


def decrypt(message, key_matrix):
    coords = []
    plaintext = []
    digraphs = parse_message(message)

    for d in digraphs:
        swap = []
        temp = []
        coords = get_coords(d, key_matrix)
        if coords[0][0] == coords[1][0]:  # digraph lies on same x axis
            x, y = ((coords[0][0], (coords[0][1] - 1) % 5))
            swap.append((x, y))
            x, y = ((coords[1][0], (coords[1][1] - 1) % 5))
            swap.append((x, y))
        elif coords[0][1] == coords[1][1]:  # digraph lies on same y axis
            x, y = (((coords[0][0] - 1) % 5), coords[0][1])
            swap.append((x, y))
            x, y = (((coords[1][0] - 1) % 5), coords[1][1])
            swap.append((x, y))
        else:  # digraph lies on different x & y axis
            swap.append((coords[0][0], coords[1][1]))
            swap.append((coords[1][0], coords[0][1]))

        for x, y in swap:
            plaintext.append(key_matrix[x][y])

    print "Your decrypted message is: %s " % ''.join(plaintext)


"""
Function: parse_message(message)
Brief: Parses the message provided by the user. 
Prepares the text by handling cases where double letters appear next to each other.
Ignores non-alphabetic characters, numbers, and punctuation.
Parameter: message - The message entered by the user.
Return: Returns an array of digraphs resulting from the given message.
"""


def parse_message(message):
    digraphs = []
    while len(message) > 0:
        digraph = message[:2]
        if len(digraph) == 1:  # trailing single chracter at the end of the message
            digraph = digraph = "%c%c" % (digraph[0], "X")
            digraphs.append(digraph)
            message = message[1:]
        elif digraph[0] == digraph[1]:  # handle double letters appearing in the same digraph
            digraph = "%c%c" % (digraph[0], "X")
            digraphs.append(digraph)
            message = message[1:]
        else:  # add the digraph to the list
            digraphs.append(digraph)
            message = message[2:]

    return digraphs


"""
Function: get_coords(digraph, key_matrix)
Brief: Returns the coordinates of the letters in the given digraph from the provided keyed matrix. 
Parameter: digraph - The two-letter digraph to lookup in the key matrix.
Parameter: key_matrix - The keyed Playfair matrix to perform the lookup on.
Return: Returns an array with the coordinates of the given digraph.
"""


def get_coords(digraph, key_matrix):
    coords = []
    for char in digraph:
        for x in xrange(5):
            for y in xrange(5):
                if key_matrix[x][y] == char:
                    coords.append((x, y))
    return coords


def main():
    m = gen_matrix('')
    print "\nInitial PLAYFAIR matrix:\n"
    print_matrix(m)

    print "Enter a key:"
    k = get_key()

    print "\nKeyed PLAYFAIR matrix:\n"
    m = gen_matrix(k)
    print_matrix(m)

    decision = ""
    while decision is not "1" and decision is not "2" and decision is not "3":
        print "Would you like to encrypt or decrypt a message?"
        print "1 - Encrypt message"
        print "2 - Decrypt Message"
        print "3 - Exit"
        print "\nDecision:"
        decision = raw_input()

        if decision == "1":
            print "\nEncrypt Message:"
            print "Enter the message you would like to encrypt. \nThe only valid characters are the letters A-Z. \nPeriods may be denoted with an X"
            message = get_message()
            print "The message you entered was: %s" % message
            ciphertext = encrypt(message, m)

        elif decision == "2":
            print "\nDecrypt Message:"
            print "Enter the message you would like to decrypt. \nThe only valid characters are the letters A-Z."
            message = get_message()
            print "The message you entered was: %s" % message
            plaintext = decrypt(message, m)

        elif decision == "3":
            print "Exiting Playfair.....!!!!!!"
            break

if __name__ == "__main__":
    main()
