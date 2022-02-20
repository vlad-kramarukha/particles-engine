from ursina import Entity


class Sphere(Entity):

    def __init__(self, x, y, z):
        super().__init__(
            model='sphere',
            position=(x, y, z),
            texture='textures/earth',
            scale=0.7
        )
