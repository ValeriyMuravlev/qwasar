def my_roman_numerals_converter(num): #345 CCCIXV
    roman_digits = ['M', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    digits = [1000, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    i = 0
    res = str()
    while (num > 0 and i < len(digits)):
        for j in range(num // digits[i]):
            res += roman_digits[i]
            num -= digits[i]
        i += 1
    return res
print(my_roman_numerals_converter(25))
