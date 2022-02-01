import time

from ursina import *
from data import *
from time import *
from random import randrange
import csv


class App(Ursina):
    def __init__(self):
        super().__init__()
        Entity(
            model='quad',
            scale=100,
            texture='white_cube',
            texture_scale=(60, 60),
            rotation_x=90,
            y=-5,
            color=color.light_gray
        )
        Entity(
            model='sphere',
            scale=1000,
            texture='textures/sky0',
            double_sided=True
        )
        with open('files/coords.csv', encoding='utf-8') as r_file:
            self.file = list(csv.reader(r_file, delimiter=","))
        EditorCamera()
        camera.world_position = (0, 0, -15)
        self.spheres = []
        self.load_process()
        self.i = 0

    def read_file(self):
        iterator = 0
        for i in self.spheres:
            if self.file[iterator][0] != 'step':
                i.position = (float(self.file[iterator][0]) * 10E9,
                              float(self.file[iterator][1]) * 10E9,
                              float(self.file[iterator][2]) * 10E9)
            else:
                pass
            print(Vec3(float(self.file[iterator][0]) * 10E9,
                                  float(self.file[iterator][1]) * 10E9,
                                  float(self.file[iterator][2]) * 10E9))
            iterator = iterator + 1

    def load_process(self):
        self.spheres.clear()
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    self.spheres.append(Entity(
                        model='sphere',
                        position=(
                            ((i + 1) * L / N) / 1.1 * 30,
                            ((j + 1) * L / N) / 1.1 * 30,
                            ((k + 1) * L / N) / 1.1 * 30
                        ),
                        color=color.brown,
                        scale=0.1
                    ))

    def update(self):
        self.read_file()

    def input(self, key):
        super().input(key)


if __name__ == '__main__':
    app = App()
    update = app.update
    app.run()
