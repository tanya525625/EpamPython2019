"""
Используя паттерн "Декоратор" реализуйте возможность дополнительно добавлять к кофе
    маршмеллоу, взбитые сливки и сироп, а затем вычислить итоговую стоимость напитка.
"""


class Component:
    def get_cost(self):
        raise NotImplementedError("Override get_cost method")


class BaseDecorator(Component):
    def __init__(self, component):
        self._component = component

    def get_cost(self):
        return self._component.get_cost()


class BaseCoffe(Component):
    def get_cost(self):
        return 90


class Whip(BaseDecorator):
    def get_cost(self):
        return self._component.get_cost() + 20


class Marshmallow(BaseDecorator):
    def get_cost(self):
        return self._component.get_cost() + 30


class Syrup(BaseDecorator):
    def get_cost(self):
        return self._component.get_cost() + 15


if __name__ == "__main__":
    coffe = BaseCoffe()
    coffe = Whip(coffe)
    coffe = Marshmallow(coffe)
    coffe = Syrup(coffe)
    print("Итоговая стоимость за кофе: {}".format(str(coffe.get_cost())))
