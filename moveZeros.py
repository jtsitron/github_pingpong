class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        ## initialize the empty array which will contain the result
        movedZeros = []
        
        ## first we find the non-zero numbers and add them to a new 
        ## array
        for number in nums:
            if number != 0:
                movedZeros.append(number)
        
        ## append the zeros at the end of the result
        for zeros in range(len(nums) - len(movedZeros)):
            movedZeros.append(0)
            
        
        return movedZeros
