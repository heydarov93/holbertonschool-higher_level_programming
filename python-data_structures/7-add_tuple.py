#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = create_updated_tuple(tuple_a)
    b = create_updated_tuple(tuple_b)
    return (a[0] + b[0], a[1] + b[1])


def create_updated_tuple(tpl=()):
    length = len(tpl)

    if length == 0:
        return (0, 0)
    if length < 2:
        tmp = list(tpl)
        tmp.append(0)
        return tuple(tmp)

    return tpl
