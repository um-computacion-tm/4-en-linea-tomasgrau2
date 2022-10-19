from game import inLine

def choose_col(game):
    try:
        col_input = input(f'Jugador {game.player} ingrese un número del 0 al 6: ')
        if col_input == "q":
            return False
        col_input = int(col_input)
        try:
            game.throw_coin(col_input)
        except TypeError:
            print('Columna llena')
    except ValueError:
        print('El valor ingresado no es correcto')
    except IndexError:
        print('Por favor, seleccione una columna del 0 al 6')    


def main():
    game = inLine()
    inLine.print_tablero(game)
    while True:
        tuki = choose_col(game)
        if tuki == False:
            break
        if game.check_winner() == True:
            print(f'El juego ha terminado. Felicitaciones jugador {game.winner}, has ganado')
            break

if __name__ == '__main__':
    main()


 