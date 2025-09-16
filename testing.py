def tgen(name: str):
    n = name.replace("_", " ")
    t = name.replace(" ", "_")
    return n, t

class tgen:
    def __init__(self, name: str):
        self.name = name.replace("_", " ")
        self.tag = name.replace(" ", "_")
        

string1 = "Places to be"

gen = tgen(string1)
print(gen.name, gen.tag)