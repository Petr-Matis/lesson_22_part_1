# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, city_population, room_num):
        self.city_population = city_population
        self.room_num = room_num

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_population


person_1 = Person(125795, 14)

person_2 = Person(734324, 44)

print(person_1.get_person_room())
print(person_2.get_person_room())
print(person_1.get_city_population())
print(person_2.get_city_population())
