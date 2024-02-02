#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {"I": 1, "V": 5, "X": 10,
           "L": 50, "C": 100, "D": 500,
           "M": 1000}
    s = roman_string

    if not s or not isinstance(s, type("str")):
        return 0

    i = 0
    result = 0
    length = len(s)

    while i < length:
        nxt = i + 1
        if nxt < length and rom[s[i]] < rom[s[nxt]]:
            result += (rom[s[nxt]] - rom[s[i]])
            i = nxt + 1
            continue
        else:
            result += rom[s[i]]
            i += 1

    return result
