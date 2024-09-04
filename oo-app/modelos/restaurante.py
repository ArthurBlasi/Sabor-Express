class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_resturantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✓' if self._ativo else 'X'

    def alterar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('Praça','Gourmet')
#restaurante_praca.nome = 'Praça'
#restaurante_praca.categoria = 'Gourmet'
restaurante_pizza = Restaurante('Pizza','Italiana') 

restaurante_praca.alterar_estado()

Restaurante.listar_resturantes()
