class Retangulo:

    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcularArea(self):
        return self.altura * self.largura

    def calcularPerimetro(self):
        return(self.altura * 2) + (self.largura * 2)

    def imprimir(self):
        print("Altura: ", self.altura, "\nLargura: ", self.largura)