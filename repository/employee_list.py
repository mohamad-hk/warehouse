import os
import pickle


def write_to_file(data_list):
    file = open('employee.dat', 'wb')
    pickle.dump(data_list, file)
    file.close()


def read_from_file():
    if not os.path.exists('employee.dat') or os.stat('employee.dat').st_size == 0:
        return []

    try:
        file = open('employee.dat', 'rb')
        data_list = pickle.load(file)
        file.close()
        return data_list
    except EOFError:
        print("Error: The file is empty.")
        return []
