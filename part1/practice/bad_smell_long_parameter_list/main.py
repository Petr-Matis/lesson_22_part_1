# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, state, speed, x, y):
        self.field = field
        self.state = state
        self.speed = speed
        self.x = x
        self.y = y

    def get_speed(self):
        if self.state == 'fly':
            self.speed = self.speed * 3
        elif self.state == 'crawl':
            self.speed = self.speed * 1
        raise ValueError('Эк тебя раскорячило!')

    def move(self, direction):
        speed = self.get_speed()
        if direction == 'UP':
            self.field.set_unit(x=self.x, y=self.y + speed, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(x=self.x, y=self.y - speed, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(x=self.x - speed, y=self.y, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(x=self.x + speed, y=self.y, unit=self)