#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l=len(sys.argv) - 1
    if l > 0:
        if l == 1:
            print("{} argument:".format(l))
        else:
            print("{} arguments:".format(l))
    else:
        print("{} arguments.".format(l))
    for i in range(1, l + 1):
        print("{}: {}".format(i, sys.argv[i]))
