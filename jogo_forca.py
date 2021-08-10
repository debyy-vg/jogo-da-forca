# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
# =========''']

# Classe
class Jogo:

    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letra_errada = []
        self.letra_certa = []


    # Método para adivinhar a letra
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letra_certa:
            self.letra_certa.append(letra)
        elif letra not in self.palavra and letra not in self.letra_errada:
            self.letra_errada.append(letra)
        else:
            return False
        return True


    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.letra_erradas == 6))


    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letra_certa:
                rtn += '_'
            else:
                rtn += letra
        return rtn


    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.letra_errada)])
        print('\n Palavra:'+ self.hide_word())
        print('\n letras erradas: ',)
        for letra in self.letra_errada:
            print(letra,)
        print()
        print('letras corretas: ',)
        for letra in self.letra_certa:
            print(letra, )
        print()






# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Jogo(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_won():
        game.print_game_status()
        user_input = input('\n digite uma letra:')
        game.guess(user_input)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
