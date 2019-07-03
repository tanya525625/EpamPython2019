"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.

"""

import yaml


class Menu:

    def __init__(self, menu_dict: dict):
        self.menu = menu_dict

    def create_dinner(self, day):
        pass

    def create_first_courses(self, day):
        pass
    
    def create_second_courses(self, day):
        pass

    def create_drinks(self, day):
        pass


class Vegan_dinner(Menu):

    def create_first_courses(self, day):
        return self.menu[day]['first_courses']['vegan']
    
    def create_second_courses(self, day):
        return self.menu[day]['second_courses']['vegan']

    def create_drinks(self, day):
        return self.menu[day]['drinks']['vegan']
    
    def create_dinner(self, day):
        print(self.create_first_courses(day))
        print(self.create_second_courses(day))
        print(self.create_drinks(day))


class Child_dinner(Menu):

    def create_first_courses(self, day):
        return self.menu[day]['first_courses']['child']
    
    def create_second_courses(self, day):
        return self.menu[day]['second_courses']['child']

    def create_drinks(self, day):
        return self.menu[day]['drinks']['child']
    
    def create_dinner(self, day):
        print(self.create_first_courses(day))
        print(self.create_second_courses(day))
        print(self.create_drinks(day))


class China_dinner(Menu):

    def create_first_courses(self, day):
        return self.menu[day]['first_courses']['china']
    
    def create_second_courses(self, day):
        return self.menu[day]['second_courses']['china']

    def create_drinks(self, day):
        return self.menu[day]['drinks']['china']
    
    def create_dinner(self, day):
        print(self.create_first_courses(day))
        print(self.create_second_courses(day))
        print(self.create_drinks(day))



menu_dict = yaml.load(open('menu.yml', encoding="utf-8"))
menu = Menu(menu_dict)

vegan_menu = Vegan_dinner(menu_dict)
child_menu = Child_dinner(menu_dict)
china_menu = China_dinner(menu_dict)

vegan_menu.create_dinner('Monday')
child_menu.create_dinner('Tuesday')
china_menu.create_dinner('Sunday')