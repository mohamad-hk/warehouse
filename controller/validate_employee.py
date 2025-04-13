import re


def check_name(first_name):
    return bool(re.search(r'^[a-zA-Z]{3,30}$', first_name))


def check_category(last_name):
    return bool(re.search(r'^[a-zA-Z]{3,30}$', last_name))


def check_phone_number(phone_number):
    return bool(re.match(r'^(09\d{9}|\+98\d{10})$', phone_number))

def check_gender(gender):
    return bool(re.search(r'^(male|female)$', gender))


def generate_id():
    pass


def check_jalali_birthdate(date_birth):
    return bool(re.match(r'^14[0-9]{2}/(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])$', date_birth))
