class Arista:
    def __init__(self, emisor, receptor, cont):
        self.emisor = emisor
        self.receptor = receptor
        self.cont = cont

    def __str__(self):
        return f'ARISTA : [{self.emisor} --> {self.receptor}:: {self.cont}]'