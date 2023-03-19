# LeetCode #217 - Contains Duplicate

def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        duplicate = set() 

        for i in range(len(nums)):
            if nums[i] in duplicate:
                return True
            duplicate.add(nums[i])
        return False

print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))