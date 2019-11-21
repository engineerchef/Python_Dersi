from json import dumps, loads


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return {"name": self.name, "price": self.price}


def total_products(products):
    total = 0.0
    for product in products:
        total += product.price
    print("Your products have a total value of : {} TL".format(total))


def load_products():
    try:
        products_file = open("products.json", "r+")
    except IOError:
        return []
    product_json = products_file.read()
    product_data = loads(product_json)

    products = []
    for product in product_data:
        products.append(Product(product['name'], product['price']))

    products_file.close()
    return products


def add_product(name, price):
    new_product = Product(name, price)
    products.append(new_product)


def list_products(products):
    for p in products:
        print("Products ({}) : Price {} TL".format(p.name, p.price))


def save_product(products):
    product_save_list = []
    for product in products:
        product_save_list.append(product.to_dict())

    products_file = open("products.json", "w+")
    products_file.write(dumps(product_save_list))
    products_file.close()


products = load_products()

while True:
    print("\n==========================\ntype 'add' to add a product")
    print("type 'quit' to quit the program")
    print("type 'total' to totally of your products")
    print("type 'list' to list all products\n==========================\n")
    command = input("type a command : ")

    if command == "quit":
        save_product(products)
        break
    if command == "add":
        product_name = input("enter a name for your product : ")
        try:
            product_price = float(input("enter price for your product  : "))
        except ValueError:
            print("enter a valid price!")
            continue
        add_product(product_name, product_price)
    if command == "list":
        list_products(products)
    if command == "total":
        total_products(products)
