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

# 1,5,10,3,9,6,13

"""

                         [1, 5, 10, 3, 9, 6, 13] 
                              (Pivot: 13)
                             /           \
                 [1, 5, 10, 3, 9, 6]      []
                     (Pivot: 6)         (Leaf)
                    /          \
              [1, 5, 3]      [10, 9]
             (Pivot: 3)     (Pivot: 9)
             /       \      /       \
           [1]       [5]  []        [10]
         (Leaf)    (Leaf) (Leaf)   (Leaf)

         once the algo has reached the base case where values are returned 

        [1]             [5]              []             [10]             []
       (Leaf)          (Leaf)           (Leaf)          (Leaf)          (Leaf)
           \             /                 \             /               /
        ([1] + 3 + [5])                 ([] + 9 + [10])                   /
          = [1, 3, 5]                 ---- = [9, 10]                      /
                 \                  /                                    /
           ([1, 3, 5] + 6 + [9, 10])                                   /
              = [1, 3, 5, 6, 9, 10]                                   /
                            \                                        /
              ([1, 3, 5, 6, 9, 10] + 13 + []) -----------------------
                    = [1, 3, 5, 6, 9, 10, 13] (Fully Sorted Result)


"""

  
