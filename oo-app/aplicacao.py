from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 10)

#restaurante_tacos = Restaurante('Tacos', 'Mexicano')
#restaurante_japa = Restaurante('Japa', 'Suhsi')

#restaurante_tacos.alterar_estado()

def main():
    Restaurante.listar_resturantes()

if __name__ == '__main__':
    main()