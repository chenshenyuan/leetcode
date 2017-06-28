
# check if two list add to odd number elements list
def sum_as_odd(a, b):
    total = len(a) + len(b)
    if total % 2 == 1:
        return True
    else:
        return False

# find out the index needed, 2 index for odd
def find_target(list1, list2):
    target_index = []
    len1 = len(list1)
    len2 = len(list2)
    if sum_as_odd(list1, list2):
        a = ( len1 +len2 ) //2 +1
        target_index.append(a)
    else:
        a = (len1 + len2) // 2
        b = (len1 + len2) // 2 + 1
        target_index.append(a)
        target_index.append(b)
    return target_index


# use to recursively find kth Numb
def find_Kth_numb(list1, list2, K):
    len1 = len(list1)
    len2 = len(list2)
    # if one of them are zero, return the kth number in another list
    # if K=1, just find the min of first numb for two list
    if len1 == 0:
        return list2[K - 1]
    elif len2 == 0:
        return list1[K - 1]
    elif K == 1:
        return min(list1[0], list2[0])
        # since list started from 0, i need to minus 1
    i = K // 2 - 1
    # if one list is less than i, the first i element of the other row will
    # never have possible, so elimite it
    if i >= len1:
        sub_str2 = list2[i:]
        k_left = K - i
        return find_Kth_numb(list1, sub_str2, k_left)
    elif i >= len2:
        sub_str1 = list1[i:]
        k_left = K - i
        return find_Kth_numb(sub_str1, list2, k_left)

        # cut the first part that has smaller number at i position
    if list1[i] > list2[i]:
        sub_str2 = list2[i + 1:]
        k_left = K - (i + 1)
        return find_Kth_numb(list1, sub_str2, k_left)
    else:
        sub_str1 = list1[i + 1:]
        k_left = K - (i + 1)
        return find_Kth_numb(sub_str1, list2, k_left)


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        # exclude the situation that there are two null list
        if len1 == 0 and len2 == 0:
            return 0

        result_list = find_target(nums1, nums2)
        result_list2 = []
        # find the target index need, two for odd sum
        for i in result_list:
            result_list2.append(find_Kth_numb(nums1, nums2, i))
        return (sum(result_list2)) / float(len(result_list2))

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


a = Solution()
print(a.findMedianSortedArrays([1],[2,3,4,5,6]))