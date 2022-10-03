from random_word import Wordnik


def words_generator(words_quantity):
    words = Wordnik()
    uniq_word = set()
    while True:
        word = words.get_random_word()
        initial_len = len(uniq_word)
        uniq_word.add(word)
        after_len = len(uniq_word)
        if after_len > initial_len:
            yield word
        else:
            continue
        if after_len == words_quantity:
            break


words = words_generator(1000)

[print(word) for word in words]

