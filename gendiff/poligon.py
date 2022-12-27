"""
Используется в качестве черновика
"""


def flatten(item):
    result = []
    for i in item:
        result += flatten(i) if isinstance(i, (list, tuple, set, )) else [i]

    return result

print(flatten([1, (2, 3), [4, 5], [], {6, 7, 8},]))
