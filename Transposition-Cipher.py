# Transposition Cipher

import pyperclip


def main():
    print('Enter the message that you want to encrypt using a transposition cipher.')
    myMessage = raw_input()
    print('Enter the key that you want to use to encrypt the message.')
    myKey = input()
    myKey = int(myKey)
    ciphertext = encryptMessage(myKey, myMessage)
    # print the encrypted string in ciphertextto the screen with a | (called a pipe character) after it in case there
    #  are spaces at the end of the encrypted message.
    print(ciphertext + '|')

    # copy the encrypted string in ciphertext to the clipboard
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    # each string in ciphertext represents a column in the grid
    ciphertext = [''] * key

    # loop through each column in ciphertext
    for col in range(key):
        pointer = col
        # keep looping until pointer goes past the length of the message

        while pointer < len(message):
            # place the character at pointer in message at the end of the current column in the ciphered text
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

    # convert the ciphterext list into a single string value and return it
    return ''.join(ciphertext)

    # if tansposition.py is run (instead of imported as a module) call the main() function


if __name__ == '__main__':
    main()
