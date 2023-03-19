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

print(containsDuplicate([1, 2, 3, 1])) #True
print(containsDuplicate([1, 2, 3, 4])) #False
print(containsDuplicate([1, 2, 3, 3])) #True