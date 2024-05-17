def index_of_by_index(word: str, lista: list[str], index: int):
    for idx, el in enumerate(lista):
        if idx < index: continue
        if el == word: return idx

    return -1


def index_of_empty(lista: list[str]):
    for idx, el in enumerate(lista):
        if el == "": return idx

    return -1


def index_of(word: str, lista: list[str]):
    for idx, el in enumerate(lista):
        if el == word: return idx

    return -1


def put(word: str, lista: list[str]):
    for idx, el in enumerate(lista):
        if el != "": continue

        lista[idx] = word
        return idx

    return -1


def remove(word: str, lista: list[str]):
    counter = 0

    for idx, el in enumerate(lista):
        if el != word: continue

        lista[idx] = ""
        counter += 1

    return counter
