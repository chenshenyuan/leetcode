# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e





class Solution(object):
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals

        initial_interval = intervals[0]
        result = [initial_interval]
        for i in range(1, len(intervals)):
            beg_numb = intervals[i].start
            end_numb = intervals[i].end
            if beg_numb > max([k.end for k in result]):
                result.append(intervals[i])
            elif end_numb < min([k.start for k in result]):
                result.append(intervals[i])
            elif end_numb >= max([k.end for k in result]) and beg_numb <= min([k.start for k in result]):
                result = []
                result.append(intervals[i])
            else:
                temp_resut = []
                for sub_interval in result:
                    if beg_numb >= sub_interval.start and end_numb <= sub_interval.end:
                        end_numb = sub_interval.end
                        beg_numb = sub_interval.start
                    elif beg_numb <= sub_interval.start and end_numb <= sub_interval.end and end_numb >= sub_interval.start:
                        end_numb = sub_interval.end
                    elif beg_numb >= sub_interval.start and end_numb >= sub_interval.end and beg_numb <= sub_interval.end:
                        beg_numb = sub_interval.start
                    elif beg_numb <= sub_interval.start and end_numb >= sub_interval.end:
                        pass
                    else:
                        temp_resut.append(sub_interval)
                intervals[i].start = beg_numb
                intervals[i].end = end_numb
                temp_resut.append(intervals[i])
                result = temp_resut

        return result

        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """