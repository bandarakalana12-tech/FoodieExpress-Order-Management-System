class Order:

    def __init__(
            self,
            customer_name,
            order_type,
            item_count,
            price_per_item,
            distance):

        self.customer_name = customer_name
        self.order_type = order_type
        self.item_count = item_count
        self.price_per_item = price_per_item
        self.distance = distance

    def calculate_food_cost(self):

        return self.item_count * self.price_per_item

    def calculate_delivery_fee(self):

        food_cost = self.calculate_food_cost()

        if food_cost > 5000:
            return 0

        return self.distance * 50

    def calculate_discount(self):

        food_cost = self.calculate_food_cost()

        if self.order_type == "Premium":
            return food_cost * 0.10

        elif self.order_type == "VIP":
            return food_cost * 0.20

        return 0

    def calculate_total(self):

        food_cost = self.calculate_food_cost()

        delivery_fee = self.calculate_delivery_fee()

        discount = self.calculate_discount()

        total = food_cost + delivery_fee - discount

        return food_cost, delivery_fee, discount, total