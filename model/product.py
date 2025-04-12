from repository.product_list import write_to_file, read_from_file


class Product:
    def __init__(self, product_id=None, product_name=None, top_category=None, mid_category=None, quantity=None):
        self.product_id = product_id
        self.product_name = product_name
        self.top_category = top_category
        self.mid_category = mid_category
        self.quantity = quantity

    def add_product(self):
        product_item = {}
        p_id = 2
        product_item["id"] = p_id
        p_name = input("Enter name of product: ")
        product_item["name"] = p_name
        p_t_category = input("Enter top_category of product: ")
        product_item["top_category"] = p_t_category
        p_m_category = input("Enter mid_category of product: ")
        product_item["mid_category"] = p_m_category
        p_quantity = int(input("Enter quantity of product: "))
        product_item["quantity"] = p_quantity
        product_list = read_from_file()
        product_list.append(product_item)
        write_to_file(product_list)

    def edit_product(self):
        new_product = {}
        products = read_from_file()
        p_id = int(input("Enter product id: "))
        temp_product = list(filter(lambda product: product["id"] == p_id, products))
        if not temp_product:
            print("Product not found!")
            return
        p_name = input(f" (old name:{temp_product[0]["name"]})=>Enter new name of product: ")
        if p_name != "":
            new_product["name"] = p_name
        else:
            new_product["name"] = temp_product[0]["name"]

        p_t_category = input(
            f"(old top category:{temp_product[0]["top_category"]})=> Enter new top_category of product: ")
        if p_t_category != "":
            new_product["top_category"] = p_t_category
        else:
            new_product["top_category"] = temp_product[0]["top_category"]

        p_m_category = input(
            f"(old mid category:{temp_product[0]["mid_category"]})=> Enter new mid_category of product: ")
        if p_m_category != "":
            new_product["mid_category"] = p_m_category
        else:
            new_product["mid_category"] = temp_product[0]["mid_category"]

        p_quantity = int(input(f"(old quantity:{temp_product[0]["quantity"]})=> Enter new quantity of product: "))
        if p_quantity != temp_product[0]["quantity"]:
            new_product["quantity"] = p_quantity
        else:
            new_product["quantity"] = temp_product[0]["quantity"]

        products = list(map(lambda product: {**product, **new_product} if product["id"] == p_id else product, products))

        write_to_file(products)

    def remove_product(self):
        products = read_from_file()
        p_id = int(input("Enter product id: "))
        product_found = list(filter(lambda product: product["id"] == p_id, products))
        if not product_found:
            print("Product not found!")
            return
        else:
            updated_product_list = list(filter(lambda product: product["id"] != p_id, products))
            write_to_file(updated_product_list)
