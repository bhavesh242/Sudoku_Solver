import constants


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


def forward_checking_with_heuristics(puzzle, domains):

    if empty_cells_num == constants.TOTAL_CELLS:
        print("The Sudoku was Solved")
        print_op(puzzle)
        return

# Optimization: We store the number of empty boxes initially and change it as we assign values, so that we do not have to recalculate them on every recurisve call


def get_initial_empty_cells(puzzle):
    global empty_cells_num
    for i in range(constants.ROWSIZE):
        for j in range(constants.COLSIZE):
            if puzzle[i][j] == 0:
                empty_cells_num = empty_cells_num + 1


def get_all_domains(puzzle):
    domains = []
    cached_boxes = {}
    for i in range(constants.ROWSIZE):
        for j in range(constants.COLSIZE):
            if puzzle[i][j] != 0:
                domains.append(None)
            else:
                domains.append(get_cell_domain(i, j, puzzle, cached_boxes))

    return domains


def get_cell_domain(row, col, puzzle, cached_boxes):
    exclude_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    box_number = row//3*3 + col//3
    box_elements = set()
    if box_number in cached_boxes.keys():
        box_elements = cached_boxes[box_number]
    else:
        box_elements = get_box_elements(box_number, puzzle)
        cached_boxes[box_number] = box_elements
    all_neighbors = box_elements.union(get_row_col_neighbors(row, col, puzzle))
    sol = exclude_set - all_neighbors
    print(str(row) + " " + str(col) + " " + str(sol))
    return sol


def get_box_elements(box_number, puzzle):
    box_elements = set()
    boxRow = box_number//3 * 3
    boxCol = box_number % 3 * 3
    for row in range(boxRow, boxRow+3):
        for col in range(boxCol, boxCol + 3):
            if(puzzle[row][col] == 0):
                continue
            else:
                box_elements.add(puzzle[row][col])
    return box_elements


def get_row_col_neighbors(row, col, puzzle):
    neighbors = set()
    for i in range(constants.ROWSIZE):
        neighbors.add(puzzle[i][col])

    for j in range(constants.COLSIZE):
        neighbors.add(puzzle[row][j])
    return neighbors


def print_op(puzzle):
    for row in range(constants.ROWSIZE):
        print(puzzle[row])


if __name__ == "__main__":
    main()
