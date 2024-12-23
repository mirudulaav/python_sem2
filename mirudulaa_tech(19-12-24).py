'''def convert_to_roman(num):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    result = ' '
    for value in roman_numerals:
        while num >= value:
            result += roman_numerals[value]
            num -= value
    return result

number = int(input("Enter number:"))
print(f"Roman numeral for {number} is {convert_to_roman(number)}")
'''
number = [
    ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
    ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
    ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
]
symbol=input("Enter the symbol: ")
result=0
for v,s in number:
    for n in symbol:
        if n==v:
            result+= s
print(result)
