arr = list(input())
for i in arr:
    if ord('a') <= ord(i) <= ord('z'):
        print("%c" % (ord(i) - 32), end="")
    else:
        print("%s" % (i), end="")
