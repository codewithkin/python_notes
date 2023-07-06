#Problem statement: Write a Python program that takes a list of numbers as input and outputs the largest number in the list.

def findLargest(nums):
    largest = nums[0]
    for num in nums[1:]:
        if(num > largest):
            largest = num
            
    return largest
        
print(findLargest([1, 2, 4, 5]))