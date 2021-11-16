import constants


empty_cells_num = None


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
    still_valid = solve_for_single_domain_cells(puzzle, domains)
    if(still_valid == False):
        print("The Puzzle is not valid")
    forward_checking_with_heuristics(puzzle, domains)


def solve_for_single_domain_cells(puzzle, domains):
    global empty_cells_num
    if(empty_cells_num == 0):
        return True
    minLen, min_len_domains = get_cells_with_minimum_domain(puzzle, domains)
    if(minLen > 1):
        return True
    if(minLen <= 0):
        return False

    for i in range(len(min_len_domains)):
        cell_num = min_len_domains[i]
        row = cell_num//9
        col = cell_num % 9
        puzzle[row][col] = next(iter(domains[cell_num]))
        empty_cells_num = empty_cells_num - 1
        filled_domains = affect_neighbors(
            cell_num, domains[cell_num], puzzle, domains)
        if(filled_domains == False):
            return False
        else:
            domains[cell_num] = None
    return solve_for_single_domain_cells(puzzle, domains)


def affect_neighbors(cell_to_change, value, puzzle, domains):
    minus = set(value)
    row = cell_to_change//9
    col = cell_to_change % 9
    for i in range(constants.COLSIZE):
        cell_num = row*9 + i
        if cell_num == cell_to_change or puzzle[row][i] != 0:
            continue
        domains[cell_num] = domains[cell_num] - minus
        if(len(domains[cell_num]) == 0):
            return False

    for i in range(constants.ROWSIZE):
        cell_num = i*9 + col
        if cell_num == cell_to_change or puzzle[i][col] != 0:
            continue
        domains[cell_num] = domains[cell_num] - minus
        if(len(domains[cell_num]) == 0):
            return False

    for i in range(row//3*3, row//3*3 + 3):
        for j in range(col//3*3, col//3*3 + 3):
            cell_num = i*9 + j
            if(cell_num == cell_to_change or puzzle[i][j] != 0):
                continue
            else:
                domains[cell_num] = domains[cell_num] - minus
                if (len(domains[cell_num]) == 0):
                    return False
    return True


def forward_checking_with_heuristics(puzzle, domains):

    if empty_cells_num == 0:
        print("The Sudoku was Solved")
        print_op(puzzle)
        return

    cell = get_cell_with_highest_heuristics(puzzle, domains)


def get_cell_with_highest_heuristics(puzzle, domains):
    min_domain_cells = get_cells_with_minimum_domain(puzzle, domains)


def get_cells_with_minimum_domain(puzzle, domains):
    minLen = float('inf')
    for x in range(constants.TOTAL_CELLS):
        if domains[x] == None:
            continue
        else:
            if len(domains[x]) < minLen:
                minLen = len(domains[x])
                if minLen == 1:
                    break
    min_len_domains = [k for k in range(constants.TOTAL_CELLS) if (
        domains[k] != None and len(domains[k]) == minLen)]
    return minLen, min_len_domains


# Optimization: We store the number of empty boxes initially and change it as we assign values, so that we do not have to recalculate them on every recurisve call
def get_initial_empty_cells(puzzle):
    global empty_cells_num
    empty_cells_num = 0
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
                cell_domain = get_cell_domain(i, j, puzzle, cached_boxes)
                if (len(cell_domain) == 0 or cell_domain == None):
                    return False
                domains.append(cell_domain)

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
