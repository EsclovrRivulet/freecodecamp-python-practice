def number_pattern(n):
    numbers = []
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        for num in range(1, n + 1):
            numbers.append(str(num))
        return ' '.join(numbers)

print(number_pattern(10))