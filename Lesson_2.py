number = 'Здравствуйте, ведите три целых числа:'
print(number)
number1 = int(input('first:'))
number2 = int(input('second:'))
number3 = int(input('third:'))
if number1 == number2 == number3:
    print(3)
elif number1 == number2 or number2 == number3 or number1 == number3:
    print(2)
else:
    print(0)
