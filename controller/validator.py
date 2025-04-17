import re
from repository.general_list import read_from_file


class Validator:
    def check_name(self, name):
        return bool(re.search(r'^[a-zA-Z]{3,30}$', name))

    def check_category(self, category):
        return bool(re.search(r'^[a-zA-Z\s]+$', category))

    def check_quantity(self, quantity):
        return isinstance(quantity, int)

    def check_phone_number(self, phone_number):
        return bool(re.match(r'^(09\d{9}|\+98\d{10})$', phone_number))

    def check_gender(self, gender):
        return bool(re.search(r'^(male|female)$', gender))

    def check_jalali_birthdate(self, date_birth):
        return bool(re.match(r'^14[0-9]{2}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$', date_birth))

    def check_id(self, id_value):
        return isinstance(id_value, int)

    def generate_id(self, file_name):
        product_list = read_from_file(file_name)
        if not product_list:
            return 1

        last_id = product_list[-1]["id"]
        return last_id + 1
