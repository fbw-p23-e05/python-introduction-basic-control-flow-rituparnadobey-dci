# Task 1 - basic math operations


for i in range(3):

    num = int(input('Please enter a number: '))
    
    if num % 2 == 0:
        print(num, 'is Even number')
    else:
        print(num, 'is Odd number')


# Task 2 - Calculate the sum of the numbers

total_sum = 0


for i in range(3):
    
    num = int(input("Enter number: "))
    
    
    total_sum += num

print('Sum of the numbers:', total_sum)

# Task 3 - Find the maximum number

max_num = 0


for i in range(5):
    
    num = int(input("Enter number: "))
    
    
    if num > max_num:
        max_num = num

print('Maximum of the numbers', max_num)

# Task 4 - finding divisors of a number

num = input("Enter number: ")

num = int(num)

divisors = []


for i in range(1, num + 1):
    
    if num % i == 0:
        divisors.append(i)


for divisor in divisors:
    print(divisor)
    
    
# Task 5 - Check if a number is even and divisible by 3

even_num = input('Please enter a number: ')
even_num = int(even_num)

if even_num % 2 <= 0:
    print(even_num,'is even and divisible by 2')
    

# Task 6 - Check if a number is positive, odd and divisible by 7

pos_num = int(input('Please enter a number: '))

if pos_num > 0 and pos_num % 2 == 1 and pos_num % 7 <= 0:
    print(pos_num,'is positive, odd and divisible by 7')

