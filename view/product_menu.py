from model.product import *


def show_product_menu():
    while True:
        print("1)Add product\n2)Edit product\n3)Remove product\n4)return")
        input_user = input("Enter your option number: ")
        product_obj = Product()
        match input_user:
            case "1":
                product_obj.add_product()
            case "2":
                product_obj.edit_product()
            case "3":
                product_obj.remove_product()
            case "4":
                return
