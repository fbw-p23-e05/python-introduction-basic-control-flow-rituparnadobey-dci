# Task 1 - comparison operators

for i in range(3):
    x = int(input('Please enter 1st value: '))
    y = int(input('Please enter 2nd value: '))

    if x == y:
        print('Both are same value')
    else:
        print('Values are different')


    if x % 2 == 0 and y % 2 == 0:
        print('Both are even numbers')
    else:
        print('Both numbers are not even')

print()



# Task 2 - convertion month name to a number of days

months = {'Jan': 31,'Feb': 28,'Mar': 31,'Apr': 30,'May': 31,'Jun': 30,'Jul': 31,'Aug': 31,'Sep': 30,'Oct': 31,'Nov': 30,'Dec': 31}

print('List of months: ')
for i in months:
    print(i)

month_name = input('Name of the month: ')
if month_name in months:
    num_days = months[month_name]
    print(month_name,'has',num_days,'days')
else:
    print('Please enter a valid month name')

    

