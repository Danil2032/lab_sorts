def main():
    input_list = [5, 2, 7, 4, 0, 9, 8, 6]
    print("Input: ", input_list)
    bubble_sort(input_list)
    print("Bubble sort: ", input_list)

    input_list = [5, 2, 7, 4, 0, 9, 8, 6]
    mergeSort(input_list)
    print("Merge sort: ", input_list)

    input_list = [5, 2, 7, 4, 0, 9, 8, 6]
    input_list = quicksort(input_list)
    print("Quick sort: ", input_list)


def bubble_sort(input_array):
    n = 1
    while n < len(input_array):
        for i in range(len(input_array) - n):
            if input_array[i] > input_array[i + 1]:
                input_array[i], input_array[i + 1] = input_array[i + 1], input_array[i]
        n += 1


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


def quicksort(seq):
    if len(seq) <= 1:
        return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)


def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi


if __name__ == '__main__':
    main()
