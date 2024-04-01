class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def display_name(self):
        print(f"Имя героя: {self.name}")

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def __str__(self):
        return f"Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


class AirHero(SuperHero):
    area = 'воздушные'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_phrase(self):
        return "True in the True_phrase"


class EarthHero(SuperHero):
    area = 'земные'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_phrase(self):
        return "True in the True_phrase"


class SpaceHero(SuperHero):
    area = 'космические'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = False

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_phrase(self):
        return "True in the True_phrase"


class Villain(SpaceHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        self.damage = self.damage ** 2

air_hero = AirHero(name="Брюс Уэйн",
                   nickname="Бэтмен",
                   superpower="Интеллект",
                   health_points=100,
                   catchphrase="Я — Бэтмен!",
                   damage=10)

earth_hero = EarthHero(name="Питер Паркер",
                       nickname="Человек-паук",
                       superpower="Паучьи способности",
                       health_points=80,
                       catchphrase="Великая сила - это великая ответственность.",
                       damage=15)

space_hero = SpaceHero(name="Кларк Кент",
                       nickname="Супермен",
                       superpower="летать, видеть через предметы, быстро бегать",
                       health_points=120,
                       catchphrase="Защищать мир от внешних и внутренних врагов!",
                       damage=20)

villain = Villain(name="Лекс Лютор",
                  nickname="Лекс",
                  superpower="Интеллект",
                  health_points=150,
                  catchphrase="Я лучший в мире!",
                  damage=25)

air_hero.double_health()
print(air_hero.health_points)  # Выводит: 10000
print(air_hero.fly)  # Выводит: True
print(air_hero.true_phrase())  # Выводит: True in the True_phrase

villain.crit()
print(villain.damage)  # Выводит: 625
