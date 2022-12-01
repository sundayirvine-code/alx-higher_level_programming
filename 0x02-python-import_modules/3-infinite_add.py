#!/usr/bin/python3
def inf_add():
    import sys
    l=len(sys.argv) - 1
    if l == 0:
        print("{}".format(0))
    else:
        add=0
        for i in range(l + 1):
            if i != 0:
                add += int(sys.argv[i])
        print("{}".format(add))
if __name__ == "__main__":
    inf_add()
