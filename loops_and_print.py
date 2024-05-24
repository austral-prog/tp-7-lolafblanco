def enumerate_list(list = ["Red", "Green", "", "White", "Black"]):
    new = []
    a = 0
    for element in list:
        if element:
            new.append(f"{a}. {element}")
            a = a+1
    return new
enumerate_list()


def enumerate_backwards(list = ["Red", "Green", "", "White", "Black"]):
    new = []
    a = 0
    for element in list:
        if element:
            new.append(f"{a}. {element[::-1]}")
            a = a+1
    return new
enumerate_backwards()
