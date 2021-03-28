class Aluno:

    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula
        self.imprimir()

    def imprimir(self):
        print("Codigo: ", self.codigo, "\nNome: ", self.nome, "\nMatricula: ", self.matricula)


class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano):
        Aluno.__init__(codigo, nome, matricula)
        self.ano = ano
        
    def imprimir(self):
        print("Ano: ", self.ano)


class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        Aluno.__init__(codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        print("Semestre: ", self.semestre)