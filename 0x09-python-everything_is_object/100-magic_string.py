#!/usr/bin/python3
def repeat(word, n, delim):
    print(*n*[word], sep=delim)


def repeat(word, n, delim):
    print(delim.join(word for _ in range(n)))




