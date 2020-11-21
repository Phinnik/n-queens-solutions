from typing import List, Tuple
import copy


def get_possible_positions(side_length: int,
                           queens_positions: List[Tuple[int, int]] = None) -> List[Tuple[int, int]]:
    if queens_positions is None or len(queens_positions) == 0:
        return [(i, j) for i in range(side_length) for j in range(side_length)]

    elif len(queens_positions) != 0:
        last_queen = queens_positions[-1]
        possible_positions = []

        for i in range(last_queen[0] + 1, side_length):
            for j in range(side_length):
                is_possible = True
                for queen_i, queen_j in queens_positions:
                    if i == queen_i or j == queen_j or abs(i - queen_i) == abs(j - queen_j):
                        is_possible = False
                if is_possible:
                    possible_positions.append((i, j))
        return possible_positions


def solve(n_queens: int,
          side_length,
          queens_positions: List[Tuple[int, int]] = None) -> List[Tuple[Tuple[int, int]]]:

    if queens_positions is None:
        queens_positions = []
    solutions = []
    possible_positions = get_possible_positions(side_length, queens_positions)

    if len(queens_positions) == n_queens:
        solutions.append(queens_positions)

    elif len(possible_positions) != 0:
        for i, j in possible_positions:
            if i == len(queens_positions):
                queens_positions_copy = copy.deepcopy(queens_positions)
                queens_positions_copy.append((i, j))
                new_solutions = solve(n_queens, side_length, queens_positions_copy)
                solutions.extend(new_solutions)

    return solutions
