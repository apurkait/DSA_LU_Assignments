def selection_sort(given_arr):
    for i in range(len(given_arr) - 1):
        position = i
        for j in range(i + 1, len(given_arr)):
            if given_arr[position] > given_arr[j]:
                position = j

        given_arr[position], given_arr[i] = given_arr[i], given_arr[position]

    return given_arr


if __name__ == '__main__':
    arr = list(map(int, input("Enter elements of array: ").split()))
    print(selection_sort(arr))
