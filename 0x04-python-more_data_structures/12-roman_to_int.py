def roman_to_int(roman_string):
    result = 0
    if type(roman_string) == str:
        large = 1
        my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for elem in roman_string[::-1]:
            if elem in my_dict:
                if my_dict[elem] < large:
                    result -= my_dict[elem]
                else:
                    result += my_dict[elem]

    return result
