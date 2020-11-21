from n_queens_solver import solve
import json


def get_solution_dataset(file_name: str = 'n_queens_solutions.json', n_queens_min: int = 1, n_queens_max: int = 5):
    solutions = dict()
    for n_queens in range(n_queens_min, n_queens_max):
        solutions[n_queens] = solve(n_queens, n_queens)

    with open(file_name, 'w') as f:
        json.dump(solutions, f)
