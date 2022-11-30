#!/usr/bin/python3
i=122
j=90
flag=0

while(i>=97 and j>=65):
    if flag == 0:
        print("{}".format(chr(i)), end='')

    else:
        print("{}".format(chr(j)), end='')

    i -= 1
    j -= 1

    if flag == 0:
        flag = 1
    else:
        flag = 0

