"""The number 1035 is the smallest integer that exhibits a non frequent property:
one its multiples, 3105 = 1035 * 3, has its same digits but in different order,
in other words, 3105, is one of the permutations of 1035.

The number 125874 is the first integer that has this property when the multiplier is 2,
thus: 125874 * 2 = 251748

Make the function search_permMult(), that receives an upper bound, nMax and a factor k
and will output the amount of pairs below nMax that are permuted when an integer of this
range is multiplied by k. The pair will be counted if the multiple is less than nMax, too

Let'see some cases:

search_permMult(10000, 7) === 1 # because we have the pair 1359, 9513
search_permMult(5000, 7) === 0 # no pairs found, as 9513 > 5000"""


def search_permMult(nMax, k):
    count = 0
    for i in range(1, (nMax//k)+1):
        if sorted(str(i)) == sorted(str(i*k)):
            count += 1
    return count

print(search_permMult(10000, 7))
print(search_permMult(5000, 7))
print(search_permMult(10000, 4))

