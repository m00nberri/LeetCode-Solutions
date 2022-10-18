class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seti = set(nums)
        if len(seti) < len(nums):
            return True
        else:
            return False