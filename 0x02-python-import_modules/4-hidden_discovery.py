#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4, re
    names = dir(hidden_4)
    for name in names:
        x=re.findall("\A__", name)
        if x:
        else:
            print("{}".format(name))
