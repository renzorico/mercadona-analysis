# mercadona_scraper/product.py

class Product:
    def __init__(self, category, name, format, price, unit):
        self.category = category
        self.name = name
        self.format = format
        self.price = price
        self.unit = unit

    def __repr__(self):
        return f"Product(category={self.category}, name={self.name}, format={self.format}, price={self.price}, unit={self.unit})"
