"""
TC: O(N!) {The complexity is bounded by the number of valid permutations of queen placements, which is close to N!, as we prune invalid branches aggressively.}
SC: O(N^2) {The space is dominated by the auxiliary N x N grid used to track attacked cells, plus O(N) for the recursion stack depth.}

Approach:

This problem is solved using a **backtracking** algorithm to find all unique solutions for placing N non-attacking queens. We attempt to place one queen per row, starting from the first row. For each row, we iterate through all columns. The key is an auxiliary N x N grid used to track which cells are already under attack (marked with a '1') by previously placed queens. When a queen is placed on a safe cell, we use the `updateGrid` helper to mark all cells in its column and both diagonals below it as attacked. We then make a recursive call for the next row. If we reach the end of the board with N queens placed, we record the solution. We **backtrack** by exploring the next column in the current row.

The problem ran successfully on LeetCode.
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def inBounds(row, col):
            return 0<=row<n and 0<=col<n

        def updateGrid(row, col, grid):
            
            new_grid = [row[:] for row in grid]
            #block column
            for i in range(row+1, n):
                new_grid[i][col] = 1 #can't place
            

            #block diagonal left
            r,c = row+1, col-1
            while inBounds(r,c):
                new_grid[r][c] = 1
                r += 1
                c -= 1
            
            r,c = row+1, col+1
            while inBounds(r,c):
                new_grid[r][c] = 1
                r += 1
                c += 1
            
            return new_grid
        
        def backtrack(row, grid, res):
            #base case
            #append if valid res
            if row >= n:
                if len(res) == n:
                    result.append(res[:][:])
                return

            #logic
            for col in range(n):
                if inBounds(row, col) and grid[row][col] == 0:
                    #place the queen
                    updated_grid = updateGrid(row, col, grid)
                    temp = ['.']*n
                    temp[col] = 'Q'
                    temp = "".join(temp)
                    res.append(temp)
                    backtrack(row+1, updated_grid, res)
                    res.pop()
        

        result = []
        grid = [[0]*n for _ in range(n)]
        backtrack(row=0, grid=grid, res = [])
        return result