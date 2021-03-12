class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        res = [intervals[0]]
        
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])  # Merge
            
            else:
                res.append(interval)
        
        return res