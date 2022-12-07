#!/usr/bin/python3
def roman_to_int(roman_string):
    l = len(roman_string)
    numeral = 0
    i = 0
    while i < l:
        try:
            curr = roman_string[i]
            nex = roman_string[i + 1]
            if curr == 'I' and nex == 'V':
                numeral += 4
                i += 2
            elif curr == 'I' and nex == 'X':
                numeral += 9
                i += 2
            elif curr == 'X' and nex == 'L':
                numeral += 40
                i += 2
            elif curr == 'X' and nex == 'C':
                numeral += 90
                i += 2
            elif curr == 'C' and nex == 'D':
                numeral += 400
                i += 2
            elif curr == 'C' and nex == 'M':
                numeral += 900
                i += 2
        except IndexError:
            if l == 1:
                curr = roman_string[0]
                if curr == 'I':
                    numeral = 1
                elif curr == 'V':
                    numeral = 5
                elif curr == 'X':
                    numeral = 10
                elif curr == 'L':
                    numeral = 50
                elif curr == 'C':
                    numeral = 100
                elif curr == 'D':
                    numeral = 500
                elif curr == 'M':
                    numeral = 1000
                return numeral
            else:
                numeral = 0
                l = len(roman_string)
                i = 0
                while i < l:
                    print(curr)
                    if curr == 'I':
                        numeral += 1
                    elif curr == 'V':
                        numeral += 5
                    elif curr == 'X':
                        numeral += 10
                    elif curr == 'L':
                        numeral += 50
                    elif curr == 'C':
                        numeral += 100
                    elif curr == 'D':
                        numeral += 500
                    elif curr == 'M':
                        numeral += 1000
                    i += 1
                return numeral
