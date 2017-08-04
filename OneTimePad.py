# One time pad

pt = "github"
k = "cipher"
otp = ""
for i in range(len(pt)):
    char = pt[i]
    if char.islower():
        otp += chr(((ord(char) - 97) + (ord(k[i]) - 97)) % 26 + 97)
    elif char.isupper():
        otp += chr(((ord(char) - 65) + (ord(k[i]) - 65)) % 26 + 65)
    elif char.isdigit():
        otp += chr(((ord(char) - 48) + (ord(k[i]) - 48)) % 10 + 48)
    else:
        otp += chr(((ord(char) - 32) + (ord(k[i]) - 32)) % 16 + 32)
print otp

ct = otp
otp_a = ""
for i in range(len(ct)):
    char = ct[i]
    if char.islower():
        otp_a += chr(((ord(char) - 97) - (ord(k[i]) - 97)) % 26 + 97)
    elif char.isupper():
        otp_a += chr(((ord(char) - 65) - (ord(k[i]) - 65)) % 26 + 65)
    elif char.isdigit():
        otp_a += chr(((ord(char) - 48) - (ord(k[i]) - 48)) % 10 + 48)
    else:
        otp_a += chr(((ord(char) - 32) - (ord(k[i]) - 32)) % 16 + 32)
print otp_a
