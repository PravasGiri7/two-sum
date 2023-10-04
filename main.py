from typing import List

def twoSum(self,nums: List[int], target: int) -> List[int]:
    index = {}  # Dictionary to store numbers and their indices
    
    for i, num in enumerate(nums):
        remaining = target - num  # Calculate the complement
        
        # Check if the remaining exists in the dictionary
        if remaining in index:
            return [index[remaining], i]  # Return the indices of the two numbers
        
        # If not found, add the current number to the dictionary
        index[num] = i
    
    return []  # If no such pair is found, return an empty list