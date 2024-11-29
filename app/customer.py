from math import sqrt


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(self, shop: dict, fuel_price: float) -> float:
        distance_to_shop = self.calculate_distance(
            self.location,
            shop.location
        )

        total_distance = distance_to_shop * 2
        fuel_cost = ((total_distance / 100)
                     * self.car.fuel_consumption
                     * fuel_price
                     )

        product_cost = sum(
            shop.products[product] * quantity
            for product, quantity
            in self.product_cart.items())

        print(f"{self.name}'s trip to the {shop.name} "
              f"costs{fuel_cost + product_cost: .2f}")
        return fuel_cost + product_cost

    @staticmethod
    def calculate_distance(loc1: list, loc2: list) -> float:
        return sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

    def update_location(self, new_location: list) -> None:
        self.location = new_location

    def update_money(self, amount: float) -> None:
        self.money -= amount
