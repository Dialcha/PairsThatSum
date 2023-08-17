from pairs import pairs_that_sum

def test_pairs_that_sum_5():
    numbers_arr = [1, 2, 3]
    target_value = 5

    result = pairs_that_sum(numbers_arr, target_value)

    expected_result = [(2, 3)]
    assert result == expected_result

def test_pairs_that_sum_12():
    numbers_arr = [1,9,5,0,20,-4,12,16,7]
    target_value = 12

    result = pairs_that_sum(numbers_arr, target_value)

    expected_result = [(5, 7), (0, 12), (-4, 16)]
    assert result == expected_result

def test_strings_in_array():
    numbers_arr = [1,9,5,'no valid',20,-4,12]
    target_value = 12

    result = pairs_that_sum(numbers_arr, target_value)

    expected_result = 'There is a string in the data, please enter valid array of integers'
    assert result == expected_result

def test_no_pairs_sum():
    numbers_arr = [1, 2, 3]
    target_value = 111

    result = pairs_that_sum(numbers_arr, target_value)

    expected_result = []
    assert result == expected_result

def test_empty_array():
    numbers_arr = []
    target_value = 5

    result = pairs_that_sum(numbers_arr, target_value)

    expected_result = 'Invalid input'
    assert result == expected_result

def test_pairs_float_numbers():
    numbers_arr = [1.0, 2.0, 3.0]
    target_value = 5

    result = pairs_that_sum(numbers_arr, target_value)

    expected_result = 'Float numbers in the array, please enter a valid array of integers'
    assert result == expected_result

# def test_invalid_input():
#     # TODO