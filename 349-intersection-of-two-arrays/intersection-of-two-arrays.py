class Solution(object):
    def intersection(self, nums1, nums2):
        # Convert both lists into sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Use the & operator to find numbers that are in both sets
        common_numbers = set1 & set2
        
        # Convert the result back into a list and return it
        return list(common_numbers)
