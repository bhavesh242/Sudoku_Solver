
ROWSIZE = 9
COLSIZE = 9
TOTAL_CELLS = 81
empty_cells_num = 0


def main():
    puzzle = [[0, 3, 0, 0, 8, 0, 0, 0, 6],
              [5, 0, 0, 2, 9, 4, 7, 1, 0],
              [0, 0, 0, 3, 0, 0, 5, 0, 0],
              [0, 0, 5, 0, 1, 0, 8, 0, 4],
              [4, 2, 0, 8, 0, 5, 0, 3, 9],
              [1, 0, 8, 0, 3, 0, 6, 0, 0],
              [0, 0, 3, 0, 0, 7, 0, 0, 0],
              [0, 4, 1, 6, 5, 3, 0, 0, 2],
              [2, 0, 0, 0, 4, 0, 0, 6, 0]]

    solve_puzzle_for_check(puzzle)


def solve_puzzle_for_check(puzzle):
    get_initial_empty_cells(puzzle)
    domains = get_all_domains(puzzle)
    forward_checking_with_heuristics(puzzle)


def forward_checking_with_heuristics(puzzle):

    if empty_cells_num == TOTAL_CELLS:
        print("The Sudoku was Solved")
        print_op(puzzle)
        return


# Optimization: We store the number of empty boxes initially and change it as we assign values, so that we do not have to recalculate them on every recurisve call
def get_initial_empty_cells(puzzle):
    global empty_cells_num
    for i in range(ROWSIZE):
        for j in range(COLSIZE):
            if puzzle[i][j] == 0:
                empty_cells_num = empty_cells_num + 1


def get_all_domains(puzzle):
    domains = []
    for i in range(ROWSIZE):
        for j in range(COLSIZE):
            if puzzle[i][j] != 0:
                domains.append(None)
            else:
                domains.append(get_cell_domain(i, j, puzzle))

    return domains


def get_cell_domain(row, col, puzzle):
    exclude_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    box_number = [row//3, col//3]
    box_elements = get_box_elements(box_number, puzzle)
    return exclude_set.intersection(box_elements)


def get_box_elements(box_number, puzzle):
    box_elements = set()
    for row in range(box_number[0]*3, (box_number[0]+1)*3):
        for col in range(box_number[1]*3, (box_number[1]+1)*3):
            if(puzzle[row][col] == 0):
                continue
            else:
                box_elements.add(puzzle[row][col])
    return box_elements


def print_op(puzzle):
    for row in range(ROWSIZE):
        print(row)


if __name__ == "__main__":
    main()
