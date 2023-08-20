def pairs_that_sum(numbers_arr, target_value):
    pairs = set()
    seen_numbers = set()

    if numbers_arr == []:
        return "Invalid input array"

    for num in numbers_arr:
        if type(num) is not int:
            return "There are invalid data types in the array. Please add only integer numbers"

        complement = target_value - num
        if complement in seen_numbers:
            pairs.add(tuple(sorted((num, complement))))
        seen_numbers.add(num)

    return list(pairs)
    