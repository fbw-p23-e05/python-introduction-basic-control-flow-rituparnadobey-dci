for i in range(3):

    x = int(input('Please enter 1st value: '))
    y = int(input('Please enter 2nd value: '))

    if x == y:
        print('Both are same value')
    elif x > y:
        print('x is greater than y')
    elif x % 2 == 0 and y % 2 == 0:
        print('Both are even numbers')
    else:
        print('Both numbers are not even')



