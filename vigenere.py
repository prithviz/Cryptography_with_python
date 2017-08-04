# vigenere cipher

from itertools import cycle

k = "google"
pt = "ihaveuploadedanappongoogleappengine"

ALPHA = "abcdefghijklmnopqrstuvwxyz"

"Encryption"
pairs = zip(pt, cycle(k))
result = ''
for pair in pairs:
    total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
    result += ALPHA[total % 26]
print result

"Decryption"
pairz = zip(result, cycle(k))
result1 = ''
for pair in pairz:
    total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
    result1 += ALPHA[total % 26]
print result1
