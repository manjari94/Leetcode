class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new = []
        intervals = sorted(intervals)
        new.append(intervals[0])
        for each in intervals:
            if each[0]<=new[-1][1]:
                new[-1][1] = max(new[-1][1],each[1])
            else:
                new.append(each)
        return new
