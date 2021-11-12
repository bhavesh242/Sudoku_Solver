
ROWSIZE = 9
COLSIZE = 9
empty_boxes_num = 0


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
    get_initial_empty_boxes(puzzle)


    if empty_boxes_num == ROWSIZE*COLSIZE:
        print("The Sudoku was Solved")
        for row in range(len(puzzle)):
            print(row)
    else:
        print(empty_boxes_num)


# Optimization: We store the number of empty boxes initially and change it as we assign values, so that we do not have to recalculate them on every recurisve call
def get_initial_empty_boxes(puzzle):
    global empty_boxes_num
    for i in range(ROWSIZE):
        for j in range(COLSIZE):
            if puzzle[i][j] == 0:
                empty_boxes_num = empty_boxes_num + 1

if __name__ == "__main__":
    main()




