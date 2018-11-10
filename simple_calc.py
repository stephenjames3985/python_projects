#!/usr/bin/python3

import sys

script, arg1, arg2, arg3 = sys.argv
arg2, arg3 = int(arg2), int(arg3)
def arithmetic(x, y, z):
    # next we perform the arithmetic that arg1 intends
    if x == 'add':
        return y + z

    elif x == 'subtract':
        return y - z

    elif x == 'multiply':
        return y * z

    elif x == 'divide':
        return y / z

if __name__ == '__main__':
    try:
        print(f'the result of the script {script} upon {arg1} is:\n')
        print(arithmetic(arg1, arg2, arg3))

    except Exception as NoMath:
        print('it seems you may not have entered a parameter correctly...')
        print(NoMath)
        exit()
