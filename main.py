class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def display_name(self):
        """Метод для вывода имени героя"""
        print(f"Имя героя: {self.name}")

    def double_health(self):
        """Метод для умножения здоровья героя на 2"""
        self.health_points *= 2

    def __str__(self):
        """Магический метод для вывода информации о герое"""
        return f"Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}"

    def __len__(self):
        """Магический метод для подсчета длины коронной фразы героя"""
        return len(self.catchphrase)


# Создание объекта класса SuperHero и применение методов
hero = SuperHero(name="Clark Kent",
                 nickname="Superman",
                 superpower="летать, видеть через предметы, быстро бегать",
                 health_points=100,
                 catchphrase="защищать мир от внешних и внутренних врагов!")

hero.display_name()  # Выводит: Имя героя: Clark Kent
hero.double_health()
print(hero.health_points)  # Выводит: 200

print(hero)  # Выводит: Прозвище: Superman, Суперспособность: летать, Здоровье: 200
print(len(hero))  # Выводит: 36
print(hero.catchphrase)
