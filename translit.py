relations = {"A": "Ф", "B": "И", "C": "С", "D": "В", "E": "У", "F": "А", "G": "П", "H": "Р", "I": "Ш", "J": "О",
             "K": "Л", "L": "Д", "M": "Ь", "N": "Т", "O": "Щ", "P": "З", "Q": "Й", "R": "К", "S": "Ы", "T": "Е",
             "U": "Г", "V": "М", "W": "Ц", "X": "Ч", "Y": "Н", "Z": "Я", "[": "х", "]": "ъ", ";": "ж", "'": "э",
             ",": "б", ".": "ю", "{": "Х", "}": "Ъ", ":": "Ж", "<": "Б", ">": "Ю"}


def change(c):
    if c.isupper():
        return relations[c.upper()]
    return relations[c.upper()].lower()


def translate(s):
    out = ''
    for elem in s:
        if elem.upper() in relations.keys():
            out += change(elem)
        else:
            out += elem
    return out


if __name__ == "__main__":
    print(translate("Ghbdtn vbh!"))
