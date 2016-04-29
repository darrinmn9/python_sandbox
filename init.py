class Truck():
    def __init__(self, name):
        self.name = name


v8 = Truck('darrin')

print(v8.name)

x = 'hi'


def sayHello():
    print('hello world')
    return 1


setattr(v8, x, sayHello)

print(v8.hi())
