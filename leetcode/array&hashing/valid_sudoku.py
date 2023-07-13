from collections import defaultdict


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            rows = set()
            count_row = 0
            
            for j in range(len(board[i])):
                ij = (i//3)*10 + j//3
                if board[i][j] != '.':
                    rows.add(board[i][j])
                    count_row += 1
                    
                    # check column
                    if board[i][j] in cols[j]:
                        return False
                    
                    cols[j].add(board[i][j])
                    
                    # check square
                    if board[i][j] in squares[ij]:
                        return False
                    
                    squares[ij].add(board[i][j])
                   
                # check row
                if (len(rows) != count_row):
                    return False
        print(squares)
        return True
    
        
if __name__ == '__main__':
    a = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    
    print(a.isValidSudoku(board))


