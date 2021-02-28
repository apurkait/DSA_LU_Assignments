def insertion_sort(given_arr):
    for i in range(len(given_arr)):
        k = given_arr[i]
        j = i - 1
        while j >= 0 and k < given_arr[j]:
            given_arr[j + 1] = given_arr[j]
            j -= 1

        given_arr[j + 1] = k

    return given_arr


if __name__ == '__main__':
    arr = list(map(int, input("Enter elements of array: ").split()))
    print(insertion_sort(arr))
