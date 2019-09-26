def bubble_sort(data_list_or_tuple):
    """
    Takes a list or tuple of numbers and sorts the list.

    Returns
    -------
    a sorted version of the parameter list, bubble sorted
    """
    data_list = list(data_list_or_tuple)
    for count, _ in enumerate(data_list, 1):
        for x in range(len(data_list)-count):
            if data_list[x] > data_list[x+1]:
                data_list[x], data_list[x+1] = data_list[x+1], data_list[x]
    return data_list


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
