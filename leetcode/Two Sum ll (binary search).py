#Two Sum ll另一種做法，因為numbers已經排列好了，所以可以用類似二分搜尋的方式做

numbers, target = [0,0,0,0,0,2,3,9,9,9,9], 5

def twosum(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low < high:
        curr = numbers[low] + numbers[high]

        if curr == target:
            return [low + 1, high + 1]
            
        if curr < target:
            low += 1
            
        else:
            high -= 1
    
print(twosum(numbers, target))
