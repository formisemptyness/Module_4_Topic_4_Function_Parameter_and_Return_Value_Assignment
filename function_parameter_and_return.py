'''
Program: function_return_value.py
Author: Joshua M McGinley
Last Date Modified: 09/21/2022

Open your python shell/command line and write a function multiply_string() that takes a string message and a
number n and returns the string with message printed n times. Make calls to your function with your favorite
class title and a number between 2 and 7. For instance, "Python!" and 4 as paramters would return
'Python!Python!Python!Python!' to the main method call, where your program would print the result:
'''


def multiply_string(message, n):
    '''A function that takes a string (message) an int (n) and prints the message n number of times '''
    again = message * n
    return again









if __name__ == '__main__':
    try:
        message = input('Enter meassage: ')
    except:
        print('Do or do not. There is no...')
    try:
        n = int(input('Enter a good number: '))
    except ValueError as err:
        print('Error, initiate containment protocol.')
    another = multiply_string(message, n)
    print(another)
