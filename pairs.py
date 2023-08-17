def pairs_that_sum(numbers_arr, target_value):
    pairs = []
    seen_numbers = []

    if numbers_arr == []:
        return 'Invalid input array'

    for num in numbers_arr:

        if type(num) is not int:
            return 'There is invalid data types in the array, please add only integer numbers'

        complement = target_value - num
        if complement in seen_numbers:
            pairs.append((num, complement))
        seen_numbers.append(num)

    return pairs

with open("pairs.txt", "r") as file:
    content = file.read()
    print(content)