class Addition:
    def __init__(self, a, b):
        self.res = a + b


if __name__ == '__main__':
    try:
        first = int(input('Enter first number: '))
        second = int(input('Enter Second Number: '))
        add = Addition(first, second)
        print(add.res)

    except ValueError:
        print('Please enter one number only')
