#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    output = []

    for i in range(list_length):
        try:
            val1 = my_list_1[i]
            val2 = my_list_2[i]

            #check whether they are integers
            try:
                res = val1 / val2
                output.append(res)
            except ZeroDivisionError:
                    print("{}".format('division by 0'))
                    output.append(0)
            except TypeError:
                print("{}".format('wrong type'))
                output.append(0)
        except IndexError:
            print("{}".format('out of range'))
        finally:
            pass

    l = len(output)
    if l < list_length:
        r = list_length - l
        for i in range(r):
            output.append(0)

    return output
