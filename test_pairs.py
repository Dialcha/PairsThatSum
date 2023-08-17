from pairs import pairs_that_sum

def test_pairs_that_sum_5():
    numbers_arr = [1, 2, 3]
    target_value = 5

    result = pairs_that_sum(numbers_arr, target_value)

    expected_result = [(3, 2)]
    assert result == expected_result

def test_pairs_that_sum_12():
    numbers_arr = [1,9,5,0,20,-4,12,16,7]
    target_value = 12

    result = pairs_that_sum(numbers_arr, target_value)

    expected_result = [(12, 0), (16, -4), (7, 5)]
    assert result == expected_result

def test_strings_in_array():
    numbers_arr = [1,9,5,'no valid',20,-4,12]
    target_value = 12

    result = pairs_that_sum(numbers_arr, target_value)

    expected_result = 'There is invalid data types in the array, please add only integer numbers'
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

    expected_result = 'Invalid input array'
    assert result == expected_result

def test_pairs_float_numbers():
    numbers_arr = [1.0, 2.0, 3.0]
    target_value = 5

    result = pairs_that_sum(numbers_arr, target_value)

    expected_result = 'There is invalid data types in the array, please add only integer numbers'
    assert result == expected_result