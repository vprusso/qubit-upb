from ortools.sat.python import cp_model


class RooksSolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self, board, solutions):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__board = board
        self.__solutions = solutions

    def on_solution_callback(self):
        solution = []
        for r in range(len(self.__board)):
            row = ""
            for c in range(len(self.__board)):
                if self.Value(self.__board[r][c]):
                    row += "R"
                else:
                    row += "."
            solution.append(row)
        self.__solutions.append(solution)

def all_n_rooks(n):
    # Create the model
    model = cp_model.CpModel()

    # Create variables for each cell in the board
    board = [[model.NewBoolVar(f"cell_{r}_{c}") for c in range(n)] for r in range(n)]

    # Add constraints for rows (exactly one rook per row)
    for r in range(n):
        model.Add(sum(board[r][c] for c in range(n)) == 1)

    # Add constraints for columns (exactly one rook per column)
    for c in range(n):
        model.Add(sum(board[r][c] for r in range(n)) == 1)

    # Create the solver
    solver = cp_model.CpSolver()

    # Find all solutions
    solutions = []
    solution_printer = RooksSolutionPrinter(board, solutions)
    solver.SearchForAllSolutions(model, solution_printer)

    # Print the solutions
    print(f"Total solutions: {len(solutions)}")
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for row in solution:
            print(row)
        print()

n = 2
all_n_rooks(n)
