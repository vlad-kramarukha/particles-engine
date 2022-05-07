from ursina import Entity
from ursina import color


class Space:

    @staticmethod
    def createSpace():
        Entity(
            model='quad',
            scale=1000,
            texture='white_cube',
            texture_scale=(60, 60),
            rotation_x=90,
            y=-50,
            color=color.light_gray
        )
        Entity(
             model='sphere',
             scale=5000,
             color=color.cyan,
             double_sided=True,
         )
