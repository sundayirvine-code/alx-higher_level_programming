#!/usr/bin/python3
import hidden_4, re
names = dir(hidden_4)
for name in names:
    x = re.findall("\A__", name)
    if x == None:
        print("{}".format(name))
