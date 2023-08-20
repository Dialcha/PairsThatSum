from pairs.pairs import pairs_that_sum

with open("data/pairs.txt", "r") as file:
    lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        try:
            numbers_str, target_str = line.split(" ")
            numbers_arr = [int(num_str) for num_str in numbers_str.split(",")]
            target_value = int(target_str)

            result = pairs_that_sum(numbers_arr, target_value)
            print(f"For array {numbers_arr} and target value {target_value}, pairs are: {result}")
        except ValueError:
            print(f"Error in line {line_number}: Invalid format")