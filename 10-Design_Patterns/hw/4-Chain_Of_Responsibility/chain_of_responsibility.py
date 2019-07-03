"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""


class Fridge:
    _next_handler = None

    def set_next(self, h):
        self._next_handler = h
        return h

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)   


class Check_eggs(Fridge):
    eggs = 0

    def handle(self, request):
        if request['eggs'] > self.eggs:
            necessary_to_buy = request['eggs'] - self.eggs
            print(f'{necessary_to_buy} eggs')
        return super().handle(request)


class Check_flour(Fridge):
    flour = 500

    def handle(self, request):
        if request['flour'] > self.flour:
            necessary_to_buy = request['flour'] - self.flour
            print(f'{necessary_to_buy} flour')
        return super().handle(request)


class Check_milk(Fridge):
    milk = 0.2

    def handle(self, request):
        if request['milk'] > self.milk:
            necessary_to_buy = request['milk'] - self.milk
            print(f'{necessary_to_buy} milk')
        return super().handle(request)


class Check_sugar(Fridge):
    sugar = 55

    def handle(self, request):
        if request['sugar'] > self.sugar:
            necessary_to_buy = request['sugar'] - self.sugar
            print(f'{necessary_to_buy} sugar')
        return super().handle(request)


class Check_oil(Fridge):
    oil = 350

    def handle(self, request):
        if request['oil'] > self.oil:
            necessary_to_buy = request['oil'] - self.oil
            print(f'{necessary_to_buy} oil')
        return super().handle(request)


class Check_butter(Fridge):
    butter = 350

    def handle(self, request):
        if request['butter'] > self.butter:
            necessary_to_buy = request['butter'] - self.butter
            print(f'{necessary_to_buy} butter')
        return super().handle(request)


recepy = {
    'eggs': 2,
    'oil': 10,
    'milk': 0.5,
    'sugar': 100,
    'butter': 120,
    'flour': 300
}

h1 = Check_eggs()
h2 = Check_flour()
h3 = Check_milk()
h4 = Check_sugar()
h5 = Check_oil()
h6 = Check_butter()
h1.set_next(h2)
h2.set_next(h3)
h3.set_next(h4)
h4.set_next(h5)
h5.set_next(h6)
h1.handle(recepy)