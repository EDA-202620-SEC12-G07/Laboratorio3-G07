def new_list():
    newlist = {
        "elements": [],
        "size": 0
    }
    return newlist


def get_element(my_list, index):
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    for position in range(my_list["size"]):
        info = my_list["elements"][position]

        if cmp_function(element, info) == 0:
            return position

    return -1