import os
import pickle


def write_to_file(data_list):
    file = open('product.dat', 'wb')
    pickle.dump(data_list, file)
    file.close()


def read_from_file():
    if not os.path.exists('product.dat') or os.stat('product.dat').st_size == 0:
        return []

    try:
        file = open('product.dat', 'rb')
        data_list = pickle.load(file)
        file.close()
        return data_list
    except EOFError:
        print("Error: The file is empty.")
        return []
