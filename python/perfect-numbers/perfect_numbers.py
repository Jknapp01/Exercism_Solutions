def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    sum = 0
    for n in range(1, number):
        if number % n == 0:
            sum += n

    if sum == number:
        return "perfect"     
    if sum > number:
        return "abundant"     
    return "deficient"
        