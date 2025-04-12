import os
import pickle


def write_to_file(data_list, name_file):
    name_file = name_file + ".dat"
    file = open(name_file, 'wb')
    pickle.dump(data_list, file)
    file.close()


def read_from_file(name_file):
    name_file = name_file + ".dat"

    if not os.path.exists(name_file) or os.stat(name_file).st_size == 0:
        return []

    try:
        file = open(name_file, 'rb')
        data_list = pickle.load(file)
        file.close()
        return data_list
    except EOFError:
        print("Error: The file is empty.")
        return []
