class CustomMap:

    def __init__(self, dictionary, func1, func2):
        self.func1 = func1
        self.func2 = func2
        self.dictionary = dictionary

    class IterMap:
        def __init__(self, iterable):
            self.count = 0
            self.dict_keys = list(iterable.dictionary.keys())
            self.iter = iterable

        def __next__(self):
            if self.count <= len(self.dict_keys) - 1:
                new_key = self.iter.func1(self.dict_keys[self.count])
                new_value = self.iter.func2(self.iter.dictionary[self.dict_keys[self.count]])
                self.count += 1
                return {new_key: new_value}
            else:
                raise StopIteration

    def __iter__(self):
        return self.IterMap(self)


dictionary = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth"}


def func_keys(x):
    return x*2


def func_values(y):
    return y+"A"


cust_map = CustomMap(dictionary, func_keys, func_values)

for i in cust_map:
    print(i)

print(list(cust_map))
