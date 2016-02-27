def reduce(accumulator, iterable, start=None):
    collection = iter(iterable)
    if start is None:
        start = next(collection)
    for item in collection:
        start = accumulator(start, item)

    return start

print(reduce(lambda x, y: x + y, [1, 2, 3, 4], 3))
