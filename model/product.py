from controller.validate_product import generate_id, check_product_name, check_category, check_quantity
from repository.general_list import read_from_file, write_to_file


class Product:
    def __init__(self, product_id=None, product_name=None, top_category=None, mid_category=None, quantity=None):
        self.product_id = product_id
        self.product_name = product_name
        self.top_category = top_category
        self.mid_category = mid_category
        self.quantity = quantity

    def add_product(self):
        product_item = {}
        p_id = generate_id()
        product_item["id"] = p_id

        while True:
            try:
                p_name = input("Enter name of product: ")
                if not check_product_name(p_name):
                    raise ValueError("Enter correct name")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                p_t_category = input("Enter top_category of product: ")
                if not check_category(p_t_category):
                    raise ValueError("Enter correct name")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                p_m_category = input("Enter mid_category of product: ")
                if not check_category(p_m_category):
                    raise ValueError("Enter correct name")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                p_quantity = int(input("Enter quantity of product: "))
                if not check_quantity(p_quantity) and p_quantity>0:
                    raise ValueError("Enter correct quantity")
                break
            except ValueError as e:
                print(e)

        product_item["name"] = p_name
        product_item["top_category"] = p_t_category
        product_item["mid_category"] = p_m_category
        product_item["quantity"] = p_quantity

        product_list = read_from_file("product")

        product_list.append(product_item)
        write_to_file(product_list, "product")

    def edit_product(self):
        new_product = {}
        products = read_from_file("product")
        try:
            p_id = int(input("Enter product id: "))
        except ValueError:
            print("Invalid ID!")
            return

        temp_product = list(filter(lambda product: product["id"] == p_id, products))
        if not temp_product:
            print("Product not found!")
            return

        while True:
            try:
                p_name = input(f"(old name: {temp_product[0]['name']}) => Enter new name of product: ")
                if p_name == "":
                    new_product["name"] = temp_product[0]["name"]
                    break
                if not check_product_name(p_name):
                    raise ValueError("Enter correct name")
                new_product["name"] = p_name
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                p_t_category = input(
                    f"(old top category: {temp_product[0]['top_category']}) => Enter new top_category: ")
                if p_t_category == "":
                    new_product["top_category"] = temp_product[0]["top_category"]
                    break
                if not check_category(p_t_category):
                    raise ValueError("Enter correct top category")
                new_product["top_category"] = p_t_category
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                p_m_category = input(
                    f"(old mid category: {temp_product[0]['mid_category']}) => Enter new mid_category: ")
                if p_m_category == "":
                    new_product["mid_category"] = temp_product[0]["mid_category"]
                    break
                if not check_category(p_m_category):
                    raise ValueError("Enter correct mid category")
                new_product["mid_category"] = p_m_category
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                p_quantity = int(input(f"(old quantity: {temp_product[0]['quantity']}) => Enter new quantity: "))
                if p_quantity == "":
                    new_product["quantity"] = temp_product[0]["quantity"]
                    break
                if not check_quantity(p_quantity):
                    raise ValueError("Enter correct quantity")
                new_product["quantity"] = p_quantity
                break
            except ValueError as e:
                print(e)

        products = list(map(lambda product: {**product, **new_product} if product["id"] == p_id else product, products))

        write_to_file(products, "product")

    def remove_product(self):
        products = read_from_file("product")
        p_id = int(input("Enter product id: "))
        product_found = list(filter(lambda product: product["id"] == p_id, products))
        if not product_found:
            print("Product not found!")
            return
        else:
            updated_product_list = list(filter(lambda product: product["id"] != p_id, products))
            write_to_file(updated_product_list, "product")
