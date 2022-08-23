


"""Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

"""


def solution(s):
    if len(s) % 2:
        s += "_"
    return [s[i-2:i] for i in range(2, len(s)+2, 2)]


print(solution("asdfadsf"))
print(solution("asdfads"))
print(solution(""))
print(solution("x"))
