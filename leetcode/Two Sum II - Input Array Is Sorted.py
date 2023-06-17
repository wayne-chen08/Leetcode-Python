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