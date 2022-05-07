from ursina import Entity
from ursina import color


class Sphere(Entity):

    def __init__(self, x, y, z):
        super().__init__(
            model='sphere',
            position=(x, y, z),
            #color=color.black,
            texture='mars.jpg',
            scale=0.7
        )
