from collections import defaultdict

d = {'hello': 'world'}

try:
    print(d['hellos'])
except:
    print('no key in dict')

x = defaultdict(lambda: 0)

x['hello'] = 'world'

print(x['hello'])

print(x['not valid'])
