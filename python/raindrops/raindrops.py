def convert(number):
    factor3 = number % 3 == 0
    factor5 = number % 5 == 0
    factor7 = number % 7 == 0
    string = ""
    if factor3:
        string += "Pling"
    if factor5:
        string += "Plang"
    if factor7:
        string += "Plong"
    return string or str(number)