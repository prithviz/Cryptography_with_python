# Affine Cipher using co-prime


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VALUES = dict(zip(LETTERS, range(len(LETTERS))))
RVALUES = dict(zip(range(len(LETTERS)), LETTERS))


def find_coprime(a):

    for i in range(26):
        if ((i * a) % 26) == 1:
            return i

    # Raise an error
    raise Exception, "The codeword %d has not a coprime, try another" % a


def encode_affine(msg, a, b):

    encoded_message = [RVALUES[(a * VALUES[i] + b) % 26] for i in msg]

    return ''.join(encoded_message)


def decode_affine(msg, a, b):

    decode_affine('FPAMPIQQWVMFPITWU', 5, 8)
    # Inverse of the modulo
    m = find_coprime(a)

    decoded_message = [RVALUES[(m * (VALUES[i] - b)) % 26] for i in msg]

    return ''.join(decoded_message)

ptxt='PROGRAMMINGPRAXIS'
print encode_affine(ptxt,5,8)
ctxt='FPAMPIQQWVMFPITWU'
print decode_affine(ctxt,5,8)