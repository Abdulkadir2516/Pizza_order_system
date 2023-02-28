class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 39.99)


class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 64.99)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turk Pizza", 54.99)


class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 29.99)


class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin Malzemesi"
        self.cost = 5.00


class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar Malzemesi"
        self.cost = 4.00


class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keci Peyniri Malzemesi"
        self.cost = 8.00


class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et Malzemesi"
        self.cost = 10.00


class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Sogan Malzemesi"
        self.cost = 1.00


class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Misir Malzemesi"
        self.cost = 2.00