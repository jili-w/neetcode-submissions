class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for rows in matrix:
            if rows[-1] >= target:
                l = 0 
                r = len(rows) - 1
                while l < r:
                    m = l + ((r - l) // 2 )
                    if rows[m] >= target:
                        r = m
                    else:
                        l = m + 1
                    
                if rows[l] == target: return True
        
        return False