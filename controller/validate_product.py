import re

from repository.general_list import read_from_file


def generate_id():
    product_list = read_from_file("product")
    if not product_list:
        return 1

    last_id = product_list[-1]["id"]
    return last_id + 1


def check_product_name(first_name):
    return bool(re.search(r'^[a-zA-Z]{3,30}$', first_name))


def check_category(category):
    return bool(re.search(r'^[a-zA-Z\s]+$', category))


def check_quantity(quantity):
    return isinstance(quantity, int)
