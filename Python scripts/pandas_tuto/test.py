import pandas as pd


BUILDER = {
    key: value
    for key, value in zip(
        ("Lineal", "2x", "Cuadrado"),
        [[1, 2, 3], [2, 4, 6], [1, 4, 9]],
    )
}

DTF = pd.DataFrame(data=BUILDER)

lin, doub, cuad = DTF.values

print(type(lin))
print(cuad)
