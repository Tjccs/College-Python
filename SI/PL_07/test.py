from jogos_sint import *

class Pawns(Game):
    def __init__(self) :
        ...
        tabuleiro_inicial = ...
        movs_possiveis = self.movimentos_possiveis(tabuleiro_inicial,'brancas')
        self.initial = GameState(
            to_move = 'brancas',
            utility = 0,
            board = tabuleiro_inicial,
            moves = movs_possiveis)

    def actions(self, state):
        "Legal moves are any square not yet taken."
        return state.moves


    def result(self, state, move):
        if move not in state.moves:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move] = state.to_move ## adiciona jogada ao dicionário (board)
        moves = list(state.moves)
        moves.remove(move) ## eliminando-a da lista de movimentos possíveis
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, moves=moves)

    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        return state.utility if player == 'X' else -state.utility

    def display(self, state):
        board = state.board
        print("Tabuleiro actual:")
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()
        if self.terminal_test(state) :
            print("FIM do Jogo")
        else :
            print("Próximo jogador:{}\n".format(state.to_move))

    def terminal_test(self, state):
        "A state is terminal if it is won or there are no empty squares."
        return state.utility != 0 or len(state.moves) == 0
