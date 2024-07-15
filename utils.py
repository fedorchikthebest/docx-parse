from string import ascii_uppercase


def to_name(name:str) -> str:
    name = name[0].upper() + name[1:].lower()
    return name

def coords_to_xl(x: int, y: int) -> str:
    return ascii_uppercase[x] + str(y + 1)