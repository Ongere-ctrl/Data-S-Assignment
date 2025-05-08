class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_items(self, item_name: str, qty: int, unit_price: float):
        self.items.append((item_name, qty, unit_price))

    def remove_item(self, item_name: str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self) -> float:
        total = sum(qty * price for _, qty, price in self.items)
        return total

    def summary(self):
        print("Cart Contents:")
        for name, qty, price in self.items:
            print(f"{name}: {qty} @ Ksh {price:.2f} each")
        print(f"Total: Ksh {self.calculate_total():.2f}\n")


class DiscountedCart(ShoppingCart):

    def __init__(self, discount_rate: float):
        super().__init__()
        self.discount_rate = discount_rate

    def calculate_total(self) -> float:
        initial_total = super().calculate_total()
        discount = initial_total * self.discount_rate
        return initial_total - discount


class TaxedCart(ShoppingCart):

    def __init__(self, tax_rate: float):
        super().__init__()
        self.tax_rate = tax_rate

    def calculate_total(self) -> float:
        initial_total = super().calculate_total()
        tax = initial_total * self.tax_rate
        return initial_total + tax


def checkout(cart: ShoppingCart):
    cart.summary()
    print(f"Final amount: Ksh {cart.calculate_total():.2f}\n")


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_items("Kiwi", 50, 79.2)
    cart.add_items("Papaya", 30, 40.3)
    cart.add_items("Guava", 10, 20.5)
    print(">>> Regular Cart <<<")
    checkout(cart)

    disc_cart = DiscountedCart(discount_rate=0.15)
    disc_cart.add_items("Papaya", 76, 6.20)
    disc_cart.add_items("Orange", 96, 11.50)
    disc_cart.add_items("Kiwi", 85, 9.60)
    print(">>> Applying a 15% Discount <<<")
    checkout(disc_cart)

    taxed_cart = TaxedCart(tax_rate=0.07)
    taxed_cart.add_items("Papaya", 5, 2.00)
    taxed_cart.add_items("Orange", 96, 11.50)
    taxed_cart.add_items("Kiwi", 3, 1.50)
    print(">>> Applying a 7% Tax <<<")
    checkout(taxed_cart)
















