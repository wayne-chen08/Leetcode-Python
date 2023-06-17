'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. 
You may not use the same element twice.

Your solution must use only constant extra space.
'''

numbers, target = [0,0,0,0,0,2,3,9,9,9,9], 5

def twosum(numbers, target):
    temp_i,temp_j = numbers[0] - 1, numbers[0] - 1
    for i in range(len(numbers) - 1):
        if numbers[i] == temp_i:
            continue
        temp_i = numbers[i]

        for j in range(i + 1,len(numbers)):
            if numbers[j] == temp_j:
                continue
            temp_j = numbers[j]
            if target == numbers[i] + numbers[j]:
                return [i + 1,j + 1]
        
    
print(twosum(numbers, target))
