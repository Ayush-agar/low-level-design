from abc import ABC

class BasePizza:

    def cost(self):
        raise NotImplementedError()


class FarmHouse(BasePizza):

    def cost(self):
        print("farmhouse")
        return 200

class GreeneWaveMexican(BasePizza):

    def cost(self):
        return 100

class ToppingDecorator(BasePizza):

    def cost(self):
        raise NotImplementedError()


class ExtraCheese(ToppingDecorator):

    def __init__(self, pizza: BasePizza):
        self.pizza = pizza

    def cost(self):
        print("extracheese")
        return self.pizza.cost() + 20

class Mashroom(ToppingDecorator):
    
    def __init__(self, pizza: BasePizza):
        self.pizza = pizza

    def cost(self):
        print("mashroom")
        return self.pizza.cost() + 30

pizza = FarmHouse()
pizza_with_mashroom = Mashroom(pizza=pizza)
# print(pizza.cost())
# print(pizza_with_mashroom.cost())
pizza_with_mashroom_and_extra_cheese = ExtraCheese(pizza=pizza_with_mashroom)
print(pizza_with_mashroom_and_extra_cheese.cost())