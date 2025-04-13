import re


def generate_id():
    pass


def check_product_name(first_name):
    return bool(re.search(r'^[a-zA-Z]{3,30}$', first_name))


def check_category(category):
    return bool(re.search(r'^[a-zA-Z\s]+$', category))


def check_quantity(quantity):
    return isinstance(quantity, int)
