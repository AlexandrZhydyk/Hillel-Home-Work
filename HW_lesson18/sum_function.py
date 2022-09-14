""" chain_sum(5)(2)() => 7
chain_sum(5)(100)(-10)() => 95"""


def chain_sum(a=None):
    if a is None:
        return 0

    def add(b=None):
        nonlocal a
        if b is None:
            return a
        a += b
        return add
    return add

print(chain_sum(5)())
print(chain_sum(5)(2)())
print(chain_sum(5)(100)(-10)())
