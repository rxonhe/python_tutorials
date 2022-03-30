# create a function that get the next n multiples of a number
# and returns a list of these multiples
# the first multiple is always the same number
def list_of_multiples(number, n):
    # create an empty list
    multiples = []
    # loop through n times
    for i in range(n):
        # add the number to the list
        multiples.append(number * (i + 1))
    # return the list
    return multiples


def list_of_multiples_2(number, n):
    return [number * (i + 1) for i in range(n)]


def list_of_multiples_3(inicial, tamanho):
    return list(map(lambda x: inicial * (x + 1), range(tamanho)))

# MAP
# map(function, iterable, ...)
# map(f(x,y), [1, 2, 3], [4, 5, 6])
# [f(1, 4), f(2, 5), f(3, 6)] -> list(resultado)


def list_of_multiples_4(inicial, tamanho):
    def elemento(idx):
        return inicial * (idx + 1)
    return list(map(elemento, range(tamanho)))


print(list_of_multiples_4(3, 10))
