def swap():
    globals()['a'], globals()['b'] = globals()['b'], globals()['a']


if __name__ == '__main__':
    a = input('Enter First variable value: ')   # value can be a string as well
    b = input('Enter Second variable value: ')  # value can be a string as well
    print('Before swapping: ', 'a = ', a, ' and b = ', b)
    swap()
    print('After swapping: ', 'a = ', a, ' and b = ', b)


# Alternate Approach commented out below:

'''def swap():
    swap.a, swap.b = swap.b, swap.a


if __name__ == '__main__':
    swap.a = input('Enter First variable value: ')   # value can be a string as well
    swap.b = input('Enter Second variable value: ')  # value can be a string as well
    print('Before swapping: ', 'a = ', swap.a, ' and b = ', swap.b)
    swap()
    print('After swapping: ', 'a = ', swap.a, ' and b = ', swap.b)'''
