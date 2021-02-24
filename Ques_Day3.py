def remove_element(given_arr, pos):
    if not given_arr:
        return []
    try:
        given_arr.pop(pos)
        return given_arr
    except IndexError:
        print('Index not present in list, deletion not possible')
        return given_arr


if __name__ == '__main__':
    arr = list(map(int, input('Enter elements to be inserted: ').split()))
    try:
        p = int(input('Enter the index of the element that needs to be removed: '))
        print(remove_element(arr, p))
    except:
        print('Mention a valid index')

