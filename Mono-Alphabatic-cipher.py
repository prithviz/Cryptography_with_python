# Monoalphabatic

def monoalphabatic_enc_dec(pt):
    '''NO MIXED CASES ARE ALLOWD '''
    if pt.islower():
        ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        KEY = ['n', 'o', 'a', 't', 'r', 'b', 'e', 'c', 'f', 'u', 'x', 'd', 'q', 'g', 'y', 'l', 'k', 'h', 'v', 'i', 'j',
               'm', 'p', 'z', 's', 'w']
        ALP_KEY = dict(zip(ALPHABET, KEY))
        result = []
        for i in range(len(pt)):
            char = pt[i]
            x = ALP_KEY.get(char)
            result.append(x)

        KEY_ALP = dict(zip(KEY, ALPHABET))
        result1 = []
        for i in range(len(result)):
            char = result[i]
            y = KEY_ALP.get(char)
            result1.append(y)
        print''.join(result), '=', ''.join(result1)

    else:
        ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
        KEY = ['N', 'O', 'A', 'T', 'R', 'B', 'E', 'C', 'F', 'U', 'X', 'D', 'Q', 'G', 'Y', 'L', 'K', 'H', 'V', 'I', 'J',
               'M', 'P', 'Z', 'S', 'W']
        ALP_KEY = dict(zip(ALPHABET, KEY))
        result = []
        for i in range(len(pt)):
            char = pt[i]
            x = ALP_KEY.get(char)
            result.append(x)

        KEY_ALP = dict(zip(KEY, ALPHABET))
        result1 = []
        for i in range(len(result)):
            char = result[i]
            y = KEY_ALP.get(char)
            result1.append(y)
        print''.join(result), '=', ''.join(result1)


monoalphabatic_enc_dec('monoalphabatic')