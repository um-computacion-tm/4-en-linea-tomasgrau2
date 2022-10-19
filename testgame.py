import unittest
from unittest.mock import patch
from main import main

@patch("builtins.print")
@patch("builtins.input")

class TestMain(unittest.TestCase):

    def test_winner_player1(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["1","0","1","0","1","0","1"]
        main()
        last_call = patched_print.call_count
        self.assertEqual(patched_print.call_args_list[last_call - 1][0][0],
                    'El juego ha terminado. Felicitaciones jugador 1, has ganado')

    def test_winner_player2(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["2","0","1","0","1","0","1","0"]
        main()
        last_call = patched_print.call_count
        self.assertEqual(patched_print.call_args_list[last_call - 1][0][0],
                    'El juego ha terminado. Felicitaciones jugador 2, has ganado')    
                    
    def test_exit(self, patched_input, patched_print, *args):
        patched_input.side_effect = "q"
        main()
        self.assertEqual(patched_print.call_count, 7)
        patched_input.assert_called_once()

    def test_winner_horizontal(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["0","0","1","1","2","2","3"]
        main()
        last_call = patched_print.call_count
        self.assertEqual(patched_print.call_args_list[last_call - 1][0][0],
                    'El juego ha terminado. Felicitaciones jugador 1, has ganado')

    def test_exceptiuon_index_error(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["9","q"]
        main()
        self.assertEqual(patched_print.call_args_list[7][0][0],
        "Por favor, seleccione una columna del 0 al 6")

    def test_exceptiuon_value_error(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["a","q"]
        main()
        self.assertEqual(patched_print.call_args_list[7][0][0],
        "El valor ingresado no es correcto")

    def test_exceptiuon_type_error(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["0","0","0","0","0","0","0","q"]
        main()
        self.assertEqual(patched_print.call_args_list[7][0][0],
        "Columna llena")
    
                    

if __name__ == '__main__':
    unittest.main()