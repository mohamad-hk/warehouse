from controller.validate_product import check_product_name
from controller.validate_transaction import check_id
from repository.general_list import read_from_file, write_to_file


def check_product(name):
    product_list = read_from_file("product")
    temp_list = list(filter(lambda product: product["name"] == name, product_list))
    if len(temp_list) > 0:
        return True
    else:
        return "There isn't any product with this name"


def check_employee(employee_id):
    employee_list = read_from_file("employee")
    temp_list = list(filter(lambda employee: employee["id"] == employee_id, employee_list))
    if len(temp_list) > 0:
        return True
    else:
        return "Your employee id is incorrect"


class Transaction:
    def __init__(self, product_name=None, quantity=None):
        self.product_name = product_name
        self.quantity = quantity

    def import_into_warehouse(self):
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
                e_id = int(input("Enter your Employee id: "))
                if not check_id(e_id):
                    raise ValueError("Enter correct name")
                break
            except ValueError as e:
                print(e)


        if check_employee(e_id) and check_product(p_name):
            p_quantity = int(input("Enter quantity of product: "))
            product_list = read_from_file("product")
            old_product = list(filter(lambda product: product["name"] == p_name, product_list))
            total_quantity = old_product[0]["quantity"] + p_quantity
            old_product[0]["quantity"] = total_quantity
            products = list(
                map(lambda product: {**product, **old_product[0]} if product["name"] == p_name else product,
                    product_list))

            write_to_file(products, "product")

    def remove_from_warehouse(self):
        p_name = input("Enter name of product: ")

        e_id = input("Enter your Employee id: ")

        if check_employee(e_id) and check_product(p_name):
            p_quantity = int(input("Enter quantity of product: "))
            product_list = read_from_file("product")

            old_product = list(filter(lambda product: product["name"] == p_name, product_list))
            if p_quantity < old_product[0]["quantity"]:
                total_quantity = old_product[0]["quantity"] - p_quantity
                old_product[0]["quantity"] = total_quantity
                products = list(
                    map(lambda product: {**product, **old_product[0]} if product["name"] == p_name else product,
                        product_list))
                write_to_file(products, "product")

            else:
                return "your requirement is bigger than stock"
