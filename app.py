from ursina import *
from data import *
from Sphere import *
from Space import *
import csv
import time


class App(Ursina):
    def __init__(self):
        super().__init__()
        self.data = initData()
        self.N = self.data[0]
        self.L = self.data[1]
        # Массив частиц
        self.spheres = []
        # Счетчик для чтения файла
        self.iterator = 0

        # Создаем сцену
        Space.createSpace()
        # Подключаем камеру
        EditorCamera()
        # Устанавливаем начальные координаты камеры
        camera.world_position = (0, 0, -15)
        # Добавляем частицы на сцену
        self.addSpheresOnScene()

        Entity(
            model='cube',
            position=(0,0,0),
            scale=self.L * 10E9,
            color=rgb(176, 0, 0, a=20),
            opacity=0.2
        )

        # Получаем данные из файла с координатами
        with open('files/coords.csv', encoding='utf-8') as r_file:
            self.file = list(csv.reader(r_file, delimiter=","))

    # Метод для рендера частиц по координатам из файла
    def render_frames(self):
        for i in self.spheres:
            if self.file[self.iterator][0] != 'step ':
                i.position = (float(self.file[self.iterator][0]) * 10E9,
                              float(self.file[self.iterator][1]) * 10E9,
                              float(self.file[self.iterator][2]) * 10E9)
            else:
                pass
            self.iterator = self.iterator + 1

    # Метод для расстановки частиц в кубе с начальными координатами
    def addSpheresOnScene(self):
        self.spheres.clear()
        WHD = self.N**(1 / 3) + 1
        for i in range(int(WHD)):
            for j in range(int(WHD)):
                for k in range(int(WHD)):
                    x = ((i + 1) * self.L / int(WHD)) / 1.1 * 30
                    y = ((j + 1) * self.L / int(WHD)) / 1.1 * 30
                    z = ((k + 1) * self.L / int(WHD)) / 1.1 * 30
                    self.spheres.append(Sphere(x, y, z))

    # Метод отрисовки кадра (вызывается N количество раз в зависимости от герцовки монитора)
    def update(self):
        self.render_frames()
        #time.sleep(0.02)

    # Метод для подключения контроллеров для управления камерой
    def input(self, key):
        super().input(key)

# Инициализация класса приложения
if __name__ == '__main__':
    app = App()
    update = app.update

    # Запуск приложения
    app.run()
