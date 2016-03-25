
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        ## take a copy of nums
        copy = nums
        
        ## first we find the non-zero numbers in the copy and put them
        ## into a right place in nums
        it = 0
        
        for number in range(len(copy)):
            ## if the number is non-zero, put it as a next element to nums
            if copy[number] != 0:
                nums[it] = copy[number]
                ## increase the iterator
                it += 1
        
        ## fill in the zeros
        for zeros in range(it , len(nums)):
            nums[zeros] = 0
