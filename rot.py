#This py is using for decrypting simple rot encryption
import sys
if len(sys.argv) > 4 or len(sys.argv) < 3:
    print "usage: python rot.py filename [number]"
elif len(sys.argv) == 3:
    filename = sys.argv[1]
    sys.stdout.write("Rot")
    num = int(sys.argv[2])
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


