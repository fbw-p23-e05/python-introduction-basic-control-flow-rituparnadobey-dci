# Task 5 - Check if a number is even and divisible by 3

even_num = input('Please enter a number: ')
even_num = int(even_num)

if even_num % 2 <= 0:
    print(even_num,'is even and divisible by 2')

# Task 6 - Check if a number is positive, odd and divisible by 7

pos_num = int(input('Please enter a number: '))

if pos_num > 0 and pos_num % 2 == 1 and pos_num % 7 <= 0:
    print(pos_num,'is positive, odd and divisible by 7')

