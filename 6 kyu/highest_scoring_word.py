import string

values = dict(zip(string.ascii_lowercase, range(1, 27)))


def get_value(word):
    return sum(values[letter] for letter in word)


def high(word_sequence):
    return max(word_sequence.split(), key=get_value)