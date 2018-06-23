import sys
if len(sys.argv) != 2:
    print "usage: python rot.py filename"
else:
    filename = sys.argv[1]
    sys.stdout.write("Rot")
    for num in range(1, 25):
        print str(num) + ":"
        for line in open(filename, 'r'):
            for c in line:
                if ord(c) >= 65 and ord(c) <= 90:
                    rc = ord(c) - 65
                    rc = (rc + num) % 26
                    rc = chr(rc + 65)
                    sys.stdout.write(rc)
                elif ord(c) >= 97 and ord(c) <= 122:
                    rc = ord(c) - 97
                    rc = (rc + num) % 26
                    rc = chr(rc + 97)
                    sys.stdout.write(rc)
                else:
                    sys.stdout.write(c)


