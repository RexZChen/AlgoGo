class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_time = []
        end_time = []
        
        for interval in intervals:
            start_time.append(interval[0])
            end_time.append(interval[1])
        
        start_time.sort()
        end_time.sort()
        
        start_idx = end_idx = 0
        res = available = 0
        
        while start_idx < len(start_time):
            if start_time[start_idx] < end_time[end_idx]:
                
                if available == 0:
                    res += 1
                else:
                    available -= 1
                
                start_idx += 1
            
            else:
                available += 1
                end_idx += 1
        
        return res