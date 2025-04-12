from model.transanction import Transaction


def show_transaction_menu():
    while True:
        print("1)Import to warehouse\n2)remove from warehouse\n3)return")
        input_user = input("Enter your option number: ")
        transaction_obj = Transaction()
        match input_user:
            case "1":
                transaction_obj.import_into_warehouse()
            case "2":
                transaction_obj.remove_from_warehouse()
            case "3":
                return
