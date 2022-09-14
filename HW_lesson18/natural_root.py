"""Your task is to check wheter a given integer is a perfect power.
If it is a perfect power, return a pair m and k with mk = n as a proof.
Otherwise return Nothing, Nil, null, NULL, None or your language's equivalent.
Note: For a perfect power, there might be several pairs. For example 81 = 3^4 = 9^2,
so (3,4) and (9,2) are valid solutions. However, the tests take care of this,
so if a number is a perfect power, return any pair that proves it."""


def isPP(n):
    power = 2
    arr = None
    while True:
        root = int((round((n**(1/power)*100)))/100)
        if root < 2:
            return arr
        if n != root**power:
            power += 1
        else:
            return [root, power]


print(isPP(56067))
print(isPP(9))
print(isPP(5))
print(isPP(125))
