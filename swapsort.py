def swapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    count = 0
    for i in range(len(L)):
        print("this is i: ", i)
        for j in range(len(L)):
            print("this is j: ", j)
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                count += 1
                print(L)
    print("Final L: ", L)
    print("count was: ", count)