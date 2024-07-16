from string import ascii_uppercase


def to_name(name:str) -> str:
    full_name = []
    for i in name:
        full_name.append(i[0].upper() + i[1:].lower())
    if len(full_name) < 3:
        full_name.append('')
    return full_name

def coords_to_xl(x: int, y: int) -> str:
    return ascii_uppercase[x] + str(y + 1)