def new_format(string):
    length = len(string)
    if length < 4:
        return string
    formatted_str = ""
    rank = 0
    for elem in string[::-1]:
        if rank < 3:
            formatted_str += elem
            rank += 1
        else:
            formatted_str += "."
            formatted_str += elem
            rank = 1
    return formatted_str[::-1]

print(new_format("12345678"))

assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")