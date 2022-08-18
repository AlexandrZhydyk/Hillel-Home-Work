"""
In this kata, you will be given a string containing numbers from a to b,
one number can be missing from these numbers, then the string will be shuffled,
you're expected to return an array of all possible missing numbers.
Examples (input => output)

Here's a string with numbers from 1 - 21, its missing one number and the string is then shuffled,
your'e expected to return a list of possible missing numbers.

1, 21, "2198765123416171890101112131415"  => [ 12, 21 ]"""


def find_number(start, stop, string):
    missed_dig = []
    missed_num = []
    complete_arr = list(map(lambda x: str(x), range(start, stop + 1)))
    for i in range(10):
        diff = "".join(complete_arr).count(str(i)) - string.count(str(i))
        if diff:
            missed_dig += [i]*diff
    if len(missed_dig) > 1:
        for i in complete_arr:
            if missed_dig == list(sorted((map(lambda x: int(x), i)))):
                missed_num.append(int(i))
    return missed_num

