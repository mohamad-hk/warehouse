from controller.validator import Validator
from repository.general_list import read_from_file, write_to_file


def check_product(name):
    product_list = read_from_file("product")
    temp_list = list(filter(lambda product: product["name"] == name, product_list))
    if len(temp_list) > 0:
        return True
    else:
        return False


def check_employee(employee_id):
    employee_list = read_from_file("employee")
    temp_list = list(filter(lambda employee: employee["id"] == employee_id, employee_list))
    if len(temp_list) > 0:
        return True
    else:
        return False


class Transaction(Validator):
    def __init__(self, product_name=None, quantity=None):
        self.product_name = product_name
        self.quantity = quantity

    def handle_transaction(self, status):
        while True:
            try:
                p_name = input("Enter name of product: ")
                prod_check = check_product(p_name)
                if not prod_check:
                    print("There is no product with the id you entered.")
                if not self.check_name(p_name):
                    raise ValueError("Enter correct name")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                e_id_input = input("Enter your Employee id: ")
                if not e_id_input.isdigit():
                    raise ValueError("id must be a number")

                e_id = int(e_id_input)

                if not self.check_id(e_id):
                    raise ValueError("Invalid id format")

                emp_check = check_employee(e_id)
                if not emp_check:
                    print("There is no employee with the id you entered.")
                    continue

                break
            except ValueError as e:
                print(e)

        p_quantity = int(input("Enter quantity of product: "))
        product_list = read_from_file("product")
        old_product = list(filter(lambda product: product["name"] == p_name, product_list))

        if status == "export" and p_quantity > old_product[0]["quantity"]:
            print("The requested quantity is bigger than the stock available")
            return

        if status == "import":
            total_quantity = old_product[0]["quantity"] + p_quantity
        else:
            total_quantity = old_product[0]["quantity"] - p_quantity

        old_product[0]["quantity"] = total_quantity

        transaction_list = read_from_file("transaction")
        employee_list = read_from_file("employee")
        employee_info = list(filter(lambda employee: employee["id"] == e_id, employee_list))

        new_transaction = {}
        new_transaction["product_name"] = p_name
        new_transaction["quantity"] = p_quantity
        new_transaction["status"] = status
        new_transaction["modified_by"] = employee_info[0]["first_name"] + " " + employee_info[0]["last_name"]

        products = list(
            map(lambda product: {**product, **old_product[0]} if product["name"] == p_name else product,
                product_list))

        transaction_list.append(new_transaction)
        write_to_file(transaction_list, "transaction")
        write_to_file(products, "product")
