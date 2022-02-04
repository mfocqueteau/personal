import sys
import os


PATH_SEP = os.path.join("a", "b")[1]


def add_relative_path(levels_up: int, path: list) -> None:
    """
    levels_up: cantidad de directorios hacia arriba
    path: ruta desde el directorio ancestro; puede ser lista vacía
    """
    current = os.getcwd().split(PATH_SEP)
    print(current)
    for _ in range(levels_up):
        current.pop()
    print(current)
    sys.path.append(PATH_SEP + os.path.join(*(current + path)) + PATH_SEP)
    print(sys.path)


# add_relative_path(1, ["relative", "path", "to", "file"])
# import <file>  # type: ignore
