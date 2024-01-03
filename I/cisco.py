from enum import Enum
from typing import List, Optional

class Sign(Enum):
    Plus = '+'
    Minus = '-'

    @staticmethod
    def other(x: 'Sign') -> 'Sign':
        if x == Sign.Plus:
            return Sign.Minus
        elif x == Sign.Minus:
            return Sign.Plus
        else:
            raise RuntimeError('Impossible case')


class CompassDirection(Enum):
    N = 'N'
    S = 'S'
    E = 'E'
    W = 'W'

class Direction(Enum):
    H = 'H'
    V = 'V'

    def to_compass_direction(self, sign: Sign) -> CompassDirection:
        if self == Direction.H:
            if sign == Sign.Plus:
                return CompassDirection.E
            elif sign == Sign.Minus:
                return CompassDirection.W
            else:
                raise RuntimeError('Impossible case')
        elif self == Direction.V:
            if sign == Sign.Plus:
                return CompassDirection.N
            elif sign == Sign.Minus:
                return CompassDirection.S
            else:
                raise RuntimeError('Impossible case')
        else:
            raise RuntimeError('Impossible case')

class Move:
    K: int
    dir: Direction
    k: Optional[int]
    sign: Optional[Sign]

    def __init__(self, K: int, dir: Direction) -> None:
        self.K = K
        self.dir = dir
        self.k = None
        self.sign = None

# Mutates moves to contain the correct values if return value is True
def construct_ones_only(x: int, moves: List[Move]) -> bool:
    n = len(moves)
    if not(
        -n <= x <= n and
        (x - (-n)) % 2 == 0
    ):
        return False

    total = 0
    for move in moves:
        move.k = 1
        move.sign = Sign.Minus
        total -= 1

    move_iter = iter(moves)
    while total < x:
        move = next(move_iter)
        move.sign = Sign.Plus
        total += 2

    return True

# Mutates moves to contain the correct values if return value is True
def construct(x: int, moves: List[Move]) -> bool:
    # WLOG only consider the non-negative case
    if x < 0:
        if construct(-x, moves):
            for move in moves:
                move.sign = Sign.other(move.sign)
            return True
        else:
            return False

    n = len(moves)
    if n == 0:
        return x == 0
    elif n == 1:
        move, = moves
        if x == 0:
            return False
        elif 1 <= x <= move.K:
            move.sign = Sign.Plus
            move.k = x
            return True
        else:
            return False
    else:
        if all(move.K == 1 for move in moves):
            return construct_ones_only(x, moves)
        else:
            if 0 <= x < n:
                two = next(move for move in moves if move.K >= 2)
                ones = [move for move in moves if move != two]

                sub_x = next(v for v in [x-2, x-1] if v % 2 == (n-1) % 2)
                assert construct_ones_only(sub_x, ones) is True
                two.k = x - sub_x
                two.sign = Sign.Plus
                return True

            elif n <= x <= sum(move.K for move in moves):
                total = 0
                for move in moves:
                    move.k = 1
                    move.sign = Sign.Plus
                    total += 1

                move_iter = iter(moves)
                while total < x:
                    move = next(move_iter)
                    if total + (move.K - 1) < x:
                        move.k = move.K
                        total += move.K - 1
                    else:  # move.K >= 1 + (x - total)
                        move.k += x-total
                        total += x-total
                return True

            else:
                return False

def solve(x: int, y: int, moves: List[Move]):
    horizontal_moves = [move for move in moves if move.dir == Direction.H]
    vertical_moves = [move for move in moves if move.dir == Direction.V]

    if construct(x, horizontal_moves) and construct(y, vertical_moves):
        print('YES')
        for move in moves:
            print(move.k, move.dir.to_compass_direction(move.sign).value)
    else:
        print('NO')

if __name__ == '__main__':
    for _ in range(int(input())):
        n, x, y = map(int, input().split())
        def read_move():
            r, dir = input().split()
            return Move(int(r), Direction(dir))
        moves = [read_move() for _ in range(n)]

        solve(-x, -y, moves)
