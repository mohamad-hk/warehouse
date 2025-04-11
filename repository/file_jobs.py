import os
import pickle


def write_to_file(data_list):
    file = open('data.dat', 'wb')
    pickle.dump(data_list, file)
    file.close()


def read_from_file():
    if not os.path.exists('data.dat'):
        return []

    file = open('data.dat', 'rb')
    data_list = pickle.load(file)
    file.close()
    return data_list
