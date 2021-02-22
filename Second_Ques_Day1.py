if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    print(pow(X, Y))  # Using standard library function

    # Alternate method (commented out below)
    '''
    res = 1
    for i in range(Y):
        res *= X
    print(res)
    
    '''
