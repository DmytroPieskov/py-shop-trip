import json
import os
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    file_name = "config.json"
    file_name = f"app/{file_name}" \
        if not os.path.exists(file_name) \
        else file_name

    with open(file_name, "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]

    customers = []
    shops = []

    for customer_data in customers_data:
        car = Car(
            customer_data["car"]["brand"],
            customer_data["car"]["fuel_consumption"]
        )

        customer = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"], car
        )

        customers.append(customer)

    for shop_data in shops_data:

        shop = Shop(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"]
        )
        shops.append(shop)

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        best_shop = None
        # best_cost = int("inf")
        best_cost = 100000

        for shop in shops:
            if all(product in shop.products
                   for product in customer.product_cart
                   ):
                total_cost = customer.calculate_trip_cost(shop, fuel_price)

                if total_cost < best_cost:
                    best_cost = total_cost
                    best_shop = shop

        if best_shop and best_cost <= customer.money:
            customer.update_location(best_shop.location)
            customer.update_money(best_cost)
#            best_shop.print_receipt(customer, best_cost)
            best_shop.print_receipt(customer)
            customer.update_location([0, 0])  # Assuming home is at [0, 0]
            print(f"{customer.name} rides home\n{customer.name} "
                  f"now has{customer.money: .2f} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
