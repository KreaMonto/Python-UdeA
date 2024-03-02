nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

pares = []
impares = []

def separar_nums(nums):
    for num in nums:
        par = num%2 == 0
        if par:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares


separar_nums(nums)

print(f'Estos son los números pares: {pares}')
print(f'Estos son los números impares: {impares}')