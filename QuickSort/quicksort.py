def quicksort(arry):
    if len(arry) < 2:
        return arry
    else:
        pivot = arry[0] # 4
        less = [i for i in arry[1:] if i <= pivot] # less = [2,1] / [1]
        greater = [i for i in arry[1:] if i > pivot] # greater = [8,9,6] / []
        return quicksort(less) + [pivot] + quicksort(greater)


    # 4,8,2,9,6,1

# draw this algo out on paper
  
