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


