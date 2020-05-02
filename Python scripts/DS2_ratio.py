class Armor:
    def __init__(self, row):
        self.name = row[0]
        self.ar = float(row[0])
        # self.w = float(row[2])
        self.var = pulp.LpVariable(self, 0, 1, pulp.LpInteger)

    def __repr__(self):
        return "Armor(%s, %f, %f)" % (self.name, self.ar, self.w)

    def getAr(self):
        return self.var * self.ar

    def getW(self):
        return self.var * self.w


datos = open("DS2_armor_DW", "r")
