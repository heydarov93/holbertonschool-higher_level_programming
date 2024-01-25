#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    power = a
    for i in range(abs(b) - 1):
        power = power * a
    return power if b > 0 else 1 / power
