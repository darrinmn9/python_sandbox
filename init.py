from collections import OrderedDict

x = {}
x['a'] = 1
x['b'] = 2

y = OrderedDict()
y['a'] = 1
y['b'] = 2

for k, v in x.items():
    print('x:', k, v)
