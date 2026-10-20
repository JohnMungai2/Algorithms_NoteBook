import random

# Generates 30 random integers between 1 and 100 (inclusive)
random_ints = [42, 17, 88, 3, 59, 91, 12, 76, 23, 65, 34, 8, 99, 51, 27, 44, 70, 19, 83, 6, 95, 38, 62, 14, 81, 49, 73, 2, 55, 31]


def selectionsort(list):
    k = 0
    for i in range(0, len(list) - 1):
        for j in range(k, len(list)):
            PlaceHolder = None
            if list[i] > list[j]:
                PlaceHolder = list[i]
                list[i] = list[j]
                list[j] = PlaceHolder
        k += 1
    return list

print(selectionsort(random_ints))

           

