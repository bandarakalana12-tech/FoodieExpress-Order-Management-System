import sqlite3


class DatabaseManager:

    def __init__(self):
        self.conn = sqlite3.connect("foodieexpress.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customer(
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Orders(
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            order_type TEXT,
            item_count INTEGER,
            price_per_item REAL,
            food_cost REAL,
            discount REAL,
            total_amount REAL,
            FOREIGN KEY(customer_id)
            REFERENCES Customer(customer_id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Delivery(
            delivery_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            distance REAL,
            delivery_fee REAL,
            FOREIGN KEY(order_id)
            REFERENCES Orders(order_id)
        )
        """)

        self.conn.commit()

    def save_order(
            self,
            customer_name,
            order_type,
            item_count,
            price_per_item,
            distance,
            food_cost,
            discount,
            delivery_fee,
            total_amount):

        self.cursor.execute(
            """
            INSERT INTO Customer(customer_name)
            VALUES(?)
            """,
            (customer_name,)
        )

        customer_id = self.cursor.lastrowid

        self.cursor.execute(
            """
            INSERT INTO Orders(
            customer_id,
            order_type,
            item_count,
            price_per_item,
            food_cost,
            discount,
            total_amount)
            VALUES(?,?,?,?,?,?,?)
            """,
            (
                customer_id,
                order_type,
                item_count,
                price_per_item,
                food_cost,
                discount,
                total_amount
            )
        )

        order_id = self.cursor.lastrowid

        self.cursor.execute(
            """
            INSERT INTO Delivery(
            order_id,
            distance,
            delivery_fee)
            VALUES(?,?,?)
            """,
            (
                order_id,
                distance,
                delivery_fee
            )
        )

        self.conn.commit()