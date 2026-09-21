class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        subsq = defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] =='.':
                    continue
                if (board[i][j] in rowset[i] or 
                    board[i][j] in colset[j] or
                    board[i][j] in subsq[(i//3,j//3)]):
                    return False
                else:
                    rowset[i].add(board[i][j])
                    colset[j].add(board[i][j])
                    subsq[(i//3,j//3)].add(board[i][j])
        return True