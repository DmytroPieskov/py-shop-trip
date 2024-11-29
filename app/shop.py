class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer: dict) -> None:
        print(f"{customer.name} rides to {self.name}\n")
        print(f"Date{{:}} 04/01/2021 12{{:}}33{{:}}41")
        print(f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought{{:}}")

        total_product_cost = 0
        for product, quantity in customer.product_cart.items():
            opc = self.products[product] * quantity

            if isinstance(opc, float) and opc.is_integer():
                opc = int(opc)

            print(f"{quantity} {product}s for {opc} dollars")
            total_product_cost += self.products[product] * quantity

        print(f"Total cost is {total_product_cost} dollars\nSee you again!\n")
