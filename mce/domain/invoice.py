from .order import Order

class Invoice:
    
    def __init__(self, order: Order):
        self._order = order
        
    
    def total(self):
        return self._order.total()
    
    def generate_text(self) -> str:
        text = f"Invoice for Order {self._order._id}\n"
        text += f"Customer: {self._order._customer._name}\n"
        text += "Items:\n"
        for line in self._order.lines:
            text += f"  {line._product._name} x{line._quantity} @ {line._product._price} each\n"
        text += f"Total: {self.total()}\n"
        return text
    