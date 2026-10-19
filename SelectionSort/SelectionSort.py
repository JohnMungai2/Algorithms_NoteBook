numbers = [23, 4, 17, 1, 30, 10, 26, 7, 20, 13]


def selectionsort(list):
    for i in range(0, len(list) - 1):
      for j in range(0, len(list) - 1):
         PlaceHolder = None
         if list[i] > list[j]:
            PlaceHolder = list[i]
            list[i] = list[j]
            list[j] = PlaceHolder
    return list

print(selectionsort(numbers))

           

