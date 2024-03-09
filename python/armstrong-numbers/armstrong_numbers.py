def is_armstrong_number(number):
    num_str = str(number)
    len_str = len(num_str)
    sum = 0

    for digits in num_str:
        sum += (int(digits) ** int(len_str))

    return sum == number