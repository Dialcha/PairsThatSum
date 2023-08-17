def pairs_that_sum(numbers_arr, target_value):
    
    pairs = []
    len_numbers = len(numbers_arr)

    for i in range(len_numbers):
        for j in range(i + 1, len_numbers):
            if numbers_arr[i] + numbers_arr[j] == target_value:
                pairs.append((numbers_arr[i], numbers_arr[j]))

    return pairs