def reduce(accumulator, iter, start=None):
    for item in iter:
        if start is None:
            start = item
        else:
            start = accumulator(start, item)

    return start

print(reduce(lambda x, y: x * y, [1, 2, 3, 4], 2))
