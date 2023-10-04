from typing import List

def twoSum(self,nums: List[int], target: int) -> List[int]:
    index = {}  
    for i, num in enumerate(nums):
        remaining = target - num         
        if remaining in index:
            return [index[remaining], i]  
        index[num] = i
    return [] 
