def enumerate_list(lista: list[str]):
    newArray = []

    for el in lista:
        if not el: continue

        newArray.append(f"{len(newArray)}. {el}")

    return newArray

def enumerate_backwards(lista: list[str]):
    newArray = []

    for el in lista:
        if not el: continue

        newArray.append(f"{len(newArray)}. {el[::-1]}")

    return newArray

