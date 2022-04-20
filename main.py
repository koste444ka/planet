import os.path
import pickle


class Planets:
    def __init__(self, name: str, sputnik: str, type1: str, rad: str, kolca: str, mass: str):
        self.name = name
        self.sputnik = sputnik
        self.type1 = type1
        self.kolca = kolca
        self.rad = rad
        self.mass = mass

    def __str__(self):
        return f'{self.name} {self.sputnik} {self.type1} {self.rad} {self.kolca} {self.mass}'

class Spisok:
    def __init__(self):
        self.planets: list[Planets] = []

    def load_planets(self, planets: list[Planets]):
        self.planets = planets

    def get_spisokplanets(self):
        for i in self.planets:
            print(i)

    def add_planet(self, name: str, type1: str, sputnik: str, kolca: str, rad: str, mass):
        self.planets.append(Planets(name, type1, sputnik, kolca, rad, mass))

    def find_planet_by_name(self, input_name: str):
        for i in self.planets:
            if i.name == input_name:
                print(i)

    def find_planet_by_mass(self, input_mass: str, input_rad: str):
        for i in self.planets:
            if i.mass == input_mass and i.rad == input_rad:
                print(i)


def load_data(list1: Spisok):
    if os.path.exists('database_planets.dat'):
        with open('database_planets.dat', 'rb') as f:
            size = pickle.load(f)
            planets = []
            for i in range(size):
                planets.append(pickle.load(f))
            list1.load_planets(planets)
    else:
        with open('database_planets.dat', 'wb') as f:
            pickle.dump(0, f)
    return list1

def save(file_name: str, data: list):
    with open(file_name, 'wb') as f:
        pickle.dump(len(data), f)
        for item in data:
            pickle.dump(item, f)


def main():
    spisok1 = load_data(Spisok())
    a = False
    while not a:
        print('''Список команд:
        1) - Добавить планету
        2) - Вывести список всех планет
        3) - Найти планету по имени
        4) - Найти планету по параметрам
        0) - Выход''')
        cmd = input('Введите номер команды: ')
        if cmd == '0':
            a = True
        elif cmd == '1':
            try:
                name = input('Название планеты:')
                sputnik = input('Количество спутников:')
                type1 = input('Тип планеты:')
                kolca = input('Количество колец:')
                rad = input('Радиус планеты:')
                mass = input('Масса планеты:')
                spisok1.add_planet(name, sputnik, type1, kolca, rad, mass)
                save('database_music.dat', spisok1.planets)
            except ValueError:
                print('Ошибка выполнения программы')
        elif cmd == '2':
            spisok1.get_spisokplanets()
        elif cmd == '3':
            spisok1.find_planet_by_name(input())
        elif cmd == '4':

            spisok1.find_planet_by_mass(input())
    print()


if __name__ == '__main__':
    main()