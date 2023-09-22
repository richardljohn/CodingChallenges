# LeetCode #217 - Contains Duplicate

def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        duplicates = set()
        i = 0

        while i < len(nums):
            if nums[i] in duplicates:
                return True
            else: 
                duplicates.add(nums[i])
                i += 1
        return False

print(containsDuplicate([1, 2, 3, 1])) #True
print(containsDuplicate([1, 2, 3, 4])) #False
print(containsDuplicate([1, 2, 3, 3])) #True