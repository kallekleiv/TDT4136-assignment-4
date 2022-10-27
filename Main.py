import Assignment


def main():

    sudokus = {
        "Easy: ": "easy.txt",
        "Medium: ": "medium.txt",
        "Hard: ": "hard.txt",
        "Very hard: ": "veryhard.txt",
    }

    for difficulty, filename in sudokus.items():
        print(difficulty)
        csp = Assignment.create_sudoku_csp(filename)
        solution = csp.backtracking_search()
        Assignment.print_sudoku_solution(solution)
        print("\n\n")


if __name__ == "__main__":
    main()
