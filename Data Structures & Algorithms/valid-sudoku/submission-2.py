class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset,colset,gridset=defaultdict(set),defaultdict(set),defaultdict(set)

        
        for r in range(9):
            for c in range(9):
                if board[r][c] !=".":
                    print(board[r][c],rowset[r])
                    if board[r][c] in rowset[r] or board[r][c] in colset[c] or board[r][c] in gridset[(r//3,c//3)]:
                        return False
                    else:
                        rowset[r].add(board[r][c])
                        colset[c].add(board[r][c])
                        gridset[(r//3,c//3)].add(board[r][c])
        return True    




        