class Circle(object):

    pi = 3.14

    def __init__(self, **params):
        self.props = params
        self.radius = params['radius']
        self.color = params['color']
        self.area = Circle.pi * (self.radius**2)

    def get_area(self):
        return self.area

    def set_radius(self, radius):
        self.radius = radius

    def get_props(self):
        return self.props

x = Circle(radius=1, color='red')
print(x.get_props())
