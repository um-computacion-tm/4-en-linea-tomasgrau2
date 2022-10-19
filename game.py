class inLine:
    def __init__(self):
        self.board = [[0 for _ in range(7)] for _ in range (6)]
        self.player = 1
        self.player1 = 1
        self.player2 = 2
        self.winner = 0
        
    def check_winner(self):
        if self.check_col() == True:
            return True
        elif self.check_row() == True:
            return True
        elif self.check_diag() == True:
            return True
        elif self.check_diag_inverse() == True:
            return True
        else:
            return False

    #Print tablero
    def print_tablero(self):
        print(" 0  1  2  3  4  5  6")
        for r in self.board:
            print (r)
            


    #Seleccionar FILA disponible
    def available(self,col):
        for row in range(5,-1,-1):
            if self.board [row][col] == 0:
                return row

   
   #Lanzar ficha
    def throw_coin(self,col):
        if self.player == 1: 
            self.board[self.available(col)][col] = self.player1    
            self.change_turn()
        else:
            self.board[self.available(col)][col] = self.player2    
            self.change_turn()


    #Cambiar turno
    def change_turn(self):
        if self.player == 1:
            self.player += 1
        else:
            self.player -= 1



    #CHEQUEAR COLUMNAS FILAS Y DIAGONALES

    def check_row(self):
        for x in range(6):
            for y in range(7 - 3):
                if self.board[x][y] == self.player1 and self.board[x][y+1] == self.player1 and self.board[x][y+2] == self.player1 and self.board[x][y+3] == self.player1:
                    self.winner = 1
                    return True
                elif self.board[x][y] == self.player2 and self.board[x][y+1] == self.player2 and self.board[x][y+2] == self.player2 and self.board[x][y+3] == self.player2:
                    self.winner = 2
                    return True
        
    def check_col(self):
        for c in range(7):
            for r in range(6-3):
                if self.board[r][c] == self.player1 and self.board[r+1][c] == self.player1 and self.board[r+2][c] == self.player1 and self.board[r+3][c] == self.player1:
                    self.winner=1
                    return True
                elif self.board[r][c] == self.player2 and self.board[r+1][c] == self.player2 and self.board[r+2][c] == self.player2 and self.board[r+3][c] == self.player2:  
                    self.winner=2
                    return True  

    #Chequear diagonal de arriba a la derecha hacia abajo a la izquierda
    def check_diag(self):
        for x in range(6-3):
            for y in range(3,7):
                if self.board[x][y] == self.player1 and self.board[x+1][y-1] == self.player1 and self.board[x+2][y-2] == self.player1 and self.board[x+3][y-3] == self.player1:
                    self.winner = 1
                    return True
                elif self.board[x][y] == self.player2 and self.board[x+1][y-1] == self.player2 and self.board[x+2][y-2] == self.player2 and self.board[x+3][y-3] == self.player2:
                    self.winner = 2
                    return True    

    # Diagonales de arriba a la izquierda hacia abajo a la derecha

    def check_diag_inverse(self):
        for x in range(6-3):
            for y in range(7-3):
                if self.board[x][y] == self.player1 and self.board[x+1][y+1] == self.player1 and self.board[x+2][y+2] == self.player1 and self.board[x+3][y+3] == self.player1:
                    self.winner = 1
                    return True
                elif self.board[x][y] == self.player2 and self.board[x+1][y+1] == self.player2 and self.board[x+2][y+2] == self.player2 and self.board[x+3][y+3] == self.player2:
                    self.winner = 2
                    return True    

        


    




    



            
                

