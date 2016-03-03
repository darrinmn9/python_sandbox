from collections import namedtuple

Dog = namedtuple('Dog', ['bark', 'run'])

my_dog = Dog(bark=5, run='run')

print(my_dog.bark, my_dog[1])
