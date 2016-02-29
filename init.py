def reduce(accumulator, iterable, start=None):
    collection = iter(iterable)
    if start is None:
        start = next(collection)
    for item in collection:
        start = accumulator(start, item)

    return start

x = iter([1, 2, 3, 4])

for item in x:
    print(item)
