
ROWSIZE = 9
COLSIZE = 9



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
    
    
    countsMap = analyzePuzzle(puzzle)
    print(countsMap)
    

def analyzePuzzle(puzzle):
    countsMap = {}
    for x in range(1,10):
        countsMap[x] = 0;
    for i in range(ROWSIZE):
        for j in range(COLSIZE):
            if puzzle[i][j] == 0:
                continue
            else:
                 countsMap[puzzle[i][j]] = countsMap[puzzle[i][j]] + 1

    return countsMap

if __name__ == "__main__":
    main()




class Cell:
    def __init__(self,i,j,domain,remainCt):
        self.i = i
        self.j = j
        self.domain = domain
        self.remainCt = remainCt