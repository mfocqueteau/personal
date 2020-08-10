'''PokeMortys!'''
import json


class Morty:
    '''Acompañante de Rick'''

    def __init__(self, mid, name, _type, rarity, Xp, Hp, Atk, Def, Spd, total, evolves, badges):
        self.mid = mid
        self.name = name
        self.type = _type
        self.rarity = rarity
        self.Xp = Xp
        self.Hp = Hp
        self.Atk = Atk
        self.Def = Def
        self.Spd = Spd
        self.total = total
        self.evolves = 0 if evolves == '' else int(evolves)
        self.badges = badges


def import_mortys(tsv_file):
    '''Retorna lista de objetos Morty, dado un tsv'''
    all_mortys = []
    with open(tsv_file, 'r') as tsv:
        data = []
        for i, line in enumerate(tsv):
            if i % 3 != 2:
                data.append(line.strip())
            else:
                separated = line.strip().split('\t')
                for att in separated:
                    data.append(att)

                all_mortys.append(Morty(*data).__dict__)
                data = []
    return all_mortys



# MORTYS = import_mortys('Mortys.tsv')
# with open('Mortys.json', 'w') as save:
#     json.dump(MORTYS, save)

# with open('Mortys.json', 'w') as file:
#     json.dump(MORTYS, file, indent=4)

with open('Mortys.json', 'r') as file:
    MORTYS = json.load(file)

for morty in MORTYS:
    print(morty)
