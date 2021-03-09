def imprimirPi ():
    print(3.14)

imprimirPi()



# Metodo que recebe parametros
# e nao tem retorno

def calcular_imprimir_area (largura, comprimento):
    area = float (largura) * float(comprimento)
    print(area)

# Executando o método
calcular_imprimir_area(2,3)



# Método que recebe parâmetros
# e retorna um valor

def calcular_area(largura, comprimento):
    area = float(largura) * float(comprimento)
    return area

# Executando o método
print(calcular_area(2,3))

