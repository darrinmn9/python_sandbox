class Truck(object):
    def __init__(self, name):
        self.name = name


v8 = Truck('darrin')

print(v8.name)

x = 'hi'


def doIter(dict):
    for item in dict.items():
        print(item)


x = {}
x['hi'] = 1
x['yo'] = 2
x['sup'] = 3
doIter(x)


def sayHello():
    print('hello world')


# print(v8.hi())
