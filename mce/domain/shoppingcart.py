from .orderline import OrderLine


class ShoppingCart:
    
    def __init__(self):
        self._items = []
        
        
    def add(self, product, quantity):
        self._items.append(OrderLine(product, quantity))
        
    
    def total(self):
        return sum(line.line_total() for line in self._items)