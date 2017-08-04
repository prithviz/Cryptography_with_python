# File decryption with caesar

def file_ceaser_decrypt(fname):
    """Enter File name with .txt format"""
    fname = str(fname)
    f = open(fname, 'r')
    lines = f.read()
    print "Decrypting for=", lines
    k = [i for i in range(1, 26)]
    for a in range(len(k)):
        print "Applying key=", k[a]
        rs = []
        for i in range(len(lines)):
            char = lines[i]
            if char.isupper():
                r = chr((ord(char) - k[a] - 65) % 26 + 65)
            elif char.islower():
                r = chr((ord(char) - k[a] - 97) % 26 + 97)
            elif char.isdigit():
                r = chr((ord(char) - k[a] - 48) % 10 + 48)
            else:
                r = chr((ord(char) - k[a] - 32) % 16 + 32)
            rs.append(r)
        print ''.join(rs)
    f.close()


file_ceaser_decrypt("1.txt")
