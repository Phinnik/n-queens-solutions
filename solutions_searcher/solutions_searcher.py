from n_queens_solver import solve


def get_solution_dict(n_queens_min: int = 1, n_queens_max: int = 5):
    solutions = dict()
    for n_queens in range(n_queens_min, n_queens_max + 1):
        solutions[n_queens] = solve(n_queens, n_queens)
        print(f'found solutions for {n_queens} queens')

    return solutions
